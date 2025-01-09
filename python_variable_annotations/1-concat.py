#!/usr/bin/env python3
""" A type-annotated function concat that takes a string str1 and a string str2 as argumenst and returns a concatenated string
"""
def concat(str1: str, str2: str) -> str:
    """concatenates two strings and returns their concatenated result

    Args:
        str1 (str): the first str.
        str2 (str): the second str.

    Return:
        str: a concatenated string.
    """

    return str1 + str2
