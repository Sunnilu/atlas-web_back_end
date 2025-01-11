#!/usr/bin/env python3
""" type-annotated function to_kv returns a tuple. """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an integer or float, and returns a tuple.

    The first element of the tuple is the string `k`,
    and the second element is the square of `v`, 
    which is returned as a float.

    Parameters:
    k (str): The key, string.
    v (Union[int, float]): The value, which can be either an integer or a float.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string `k`, 
    and the second element is the square of `v` as a float.
    """

    # Return a tuple with the string k and the square of v (as a float)
    return (k, float(v ** 2))
