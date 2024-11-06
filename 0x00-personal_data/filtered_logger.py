#!/usr/bin/env python3
"""
This module provides functions for logging with sensitive data anonymization.
"""
from typing import List
import re
import logging
import os
import mysql.connector


# PII_FIELDS constant containing fields that need to be redacted
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Replaces specified fields in a log message with a redacted version
    """
    for field in fields:
        pattern = rf'{field}=[^{separator}]+'
        message = re.sub(pattern, f"{field}={redaction}", message)

    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Redacts sensitive fields in the log record message.
        """
        msg = super().format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt


def get_logger() -> logging.Logger:
    """
    Creates a new logger for user data.
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # StreamHandler
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db():
    """
    Connect to the MySQL database using credentials from environment
    variables and return the connection object.
    """
    # Fetching environment variables, using defaults if not set
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    # Check if the db_name is provided in the environment
    if not db_name:
        raise ValueError("Database name (PERSONAL_DATA_DB_NAME) is required")

    # Establishing a connection to the database
    connection = mysql.connector.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
    )

    return connection
