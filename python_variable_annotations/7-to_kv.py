#!/usr/bin/env python3
""" type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. """

from type import List, Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))