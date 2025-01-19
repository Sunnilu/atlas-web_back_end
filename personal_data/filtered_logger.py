#!/usr/bin/env python3
'''filter_datum that returns the log message obfuscated'''


import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str: