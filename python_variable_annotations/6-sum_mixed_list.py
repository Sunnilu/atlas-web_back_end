#!/usr/bin/env python3
"""annotated function sum_mixed_list returns their sum as a float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ a type-annotated function
    which takes a list mxd_lst of integers
    floats and returns their sum as a float.
    """
    sum = 0
    for i in mxd_lst:
        if isinstance(i, (float, int)):
            sum += i
    return sum
