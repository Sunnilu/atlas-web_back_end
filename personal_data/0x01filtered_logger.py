#!/usr/bin/env python3
"""
Module that logs filtered user data from a MySQL database.
"""
import re
def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """Return log message with specified fields obfuscated using regex substitution."""
    return re.sub(rf"({'|'.join(map(re.escape, fields))})=[^{}]*", r"\1=" + redaction, message)
