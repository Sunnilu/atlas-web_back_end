#!/usr/bin/env python3
""" type-annotated function make_multiplier multiplies float by multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number specified multiplier.

    Parameters:
    multiplier (float): The value by which other numbers will be multiplied.

    Returns:
    Callable[[float], float]: A function that takes a float returns product
    of that float and the multiplier.
    """

    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the multiplier.

        Parameters:
        value (float): The number to be multiplied.

        Returns:
        float: The result of multiplying the input value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
