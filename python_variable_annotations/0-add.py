#!/usr/bin/env 
"""
Script for a type_annotated function 'add' that takes a float 'a' and a float 'b' as agruments and returns their sum as a float
"""

def add(a: float, b: float) -> float:
    """Adds two floats and returns the sum.
    
    Args:
        a (float): the first number.
        b (float): the second number.

    Returns:
        float: The sum of 'a' and 'b'
    """
    return a + b