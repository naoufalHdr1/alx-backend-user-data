#!/usr/bin/env python3
"""
This module provides functions for logging with sensitive data anonymization.
"""
from typing import List
import re
import logging


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
