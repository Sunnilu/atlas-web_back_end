#!/usr/bin/env python3
'''filter_datum that returns the log message obfuscated'''


import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(r'(' + '|'.join(map(re.escape, fields)) + r')' + re.escape(separator) + r'([^' + re.escape(separator) + r']*)', lambda m: m.group(0).replace(m.group(2), redaction), message)
