#!/usr/bin/env python3
"""
Module that logs filtered user data from a MySQL database.
"""
import re
import os
import logging
import mysql.connector
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(
        rf'({"|".join(fields)})=[^{separator}]*',
        lambda match: f"{match.group(1)}={redaction}",
        message
    )
