#!/usr/bin/env python3
'''filter_datum that returns the log message obfuscated'''


import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'(' + '|'.join(map(re.escape, fields)) + r')' + re.escape(separator) + r'[^' + re.escape(separator) + r']*', lambda m: m.group(0).replace(m.group(0).split(separator)[-1], redaction), message)
