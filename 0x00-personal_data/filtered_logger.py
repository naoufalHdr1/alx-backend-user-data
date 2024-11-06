#!/usr/bin/env python3
"""
This module provides functions for logging with sensitive data anonymization.
"""
from typing import List
import re


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
