#!/usr/bin/env python3
"""
Module that logs filtered user data from a MySQL database.
"""

import os
import logging
import mysql.connector
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Replace occurrences of sensitive fields in a log message with a redaction string.
    """
    for field in fields:
        message = message.replace(f"{field}=", f"{field}={redaction}")
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting formatter that obfuscates PII fields in log messages.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] user_data INFO %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Apply redaction to log record.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Set up and return a logger configured to filter PII fields.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db():
    """
    Connect to a MySQL database using credentials from environment variables.
    """
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME", "")
    )


def main():
    """
    Main function that fetches and logs data from the users table,
    redacting sensitive fields.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]
    logger = get_logger()

    for row in cursor:
        message = "; ".join(f"{field}={value}" for field, value in zip(fields, row)) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
