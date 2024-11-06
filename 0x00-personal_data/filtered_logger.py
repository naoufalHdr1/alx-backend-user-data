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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database using credentials from environment
    variables and return the connection object.
    """
    # Fetching environment variables, using defaults if not set
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")

    # Establishing a connection to the database
    connection = mysql.connector.connect(
            port=3306,
            user=db_user,
            password=db_pwd,
            host=db_host,
            database=db_name
    )

    return connection


def main():
    """
    Main function to connect to the database, retrieve user data,
    and log it with redacted fields.
    """
    db = get_db()
    cursor = db.cursor()

    # Execute the query to fetch all rows in the users table
    cursor.execute("SELECT * FROM users;")

    # Loop through the rows and log the filtered (redacted) data
    for row in cursor:
        # Convert row into a dictionary with appropriate field names
        user_data = {
            'name': row[0],
            'email': row[1],
            'phone': row[2],
            'ssn': row[3],
            'password': row[4],
            'ip': row[5],
            'last_login': row[6],
            'user_agent': row[7]
        }

        # Format the log message
        log_message = f"name={user_data['name']}; email={user_data['email']}; phone={user_data['phone']}; ssn={user_data['ssn']}; password={user_data['password']}; ip={user_data['ip']}; last_login={user_data['last_login']}; user_agent={user_data['user_agent']};"

        # Redact sensitive fields in the log message
        logger = get_db()  # Get logger instance
        logger.info(filter_datum(PII_FIELDS, "***", log_message, ";"))

    cursor.close()
    db.close()


if __name__ = "__main__":
    main()
