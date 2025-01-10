#!/usr/bin/env python3
"""Annotate the below functions parameters and return values with the appropriate types"""


from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    jls_extract_var = """
        Takes a list of strings and returns a list of tuples, where each tuple contains 
        a string and its length.
    
        Parameters:
        lst (List[str]): A list of strings.
        2nd (List[Tulpes]): A string and its length.
    
        Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains a string 
        and its length as an integer.
        """
    jls_extract_var
    
    # Create a list of tuples containing the string and its length
    return [(i, len(i)) for i in lst]
