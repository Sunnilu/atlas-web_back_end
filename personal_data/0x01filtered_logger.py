#!/usr/bin/env python3
"""
Module that logs filtered user data from a MySQL database.
"""
import os
import re
import logging
import mysql.connector
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Redacts values of specified fields within a log message.

    Args:
        fields (List[str]): List of fields to redact.
        redaction (str): Redaction string to replace sensitive values.
        message (str): Original log message string.
        separator (str): Character separating each field in the log.

    Returns:
        str: Log message with specified fields redacted.
    """
    return re.sub(
        rf'({"|".join(fields)})=.*?(?={separator})',
        lambda m: f"{m.group(1)}={redaction}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """
    Redacting formatter that obfuscates PII fields in log messages.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] user_data INFO %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter.

        Args:
            fields (List[str]): List of fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format and redact sensitive fields in log record.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: Redacted log message.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Set up and return a logger configured to filter PII fields.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to a MySQL database using credentials from environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object.
    """
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME", "")
    )


def main() -> None:
    """
    Main function that fetches and logs data from the users table,
    redacting sensitive fields.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    fields = [desc[0] for desc in cursor.description]
    logger = get_logger()

    for row in cursor:
        message = "; ".join(f"{field}={value}" for field, value in zip(fields, row)) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
