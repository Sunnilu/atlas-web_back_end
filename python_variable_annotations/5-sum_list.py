#!/usr/bin/env python3
"""annotated function sum_list returns their sum as a float"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """which takes a list input_list of
    floats as argument and returns their sum as a float.
    """
    sum = 0
    for i in input_list:
        if isinstance(i, float): 
            sum += i
    return sum
