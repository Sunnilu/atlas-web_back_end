#!/usr/bin/env python3
"""Annotate the below functions parameters and return values with the appropriate types"""


from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings and returns a list of tuples, where each tuple contains 
    a string and its length.

    Parameters:
    lst (List[str]): A list of strings to be processed.

    Returns:
    List[Tuple[str, int]]: A list of tuples, where each tuple contains a string
    and its corresponding length as an integer.
    """
    
    # Generate a list of tuples (string, length of string)
    return [(i, len(i)) for i in lst]
