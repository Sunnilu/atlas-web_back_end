#!/usr/bin/env python3
""" asynchronous coroutine that takes in an integer argument."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay.


    Parameters:
    max_delay (int): The maximum delay time (default is 10seconds).


    Returns:
    float: The random delay that was waited.
    """


    delay = random.uiform(0,max_delay)

    await asyncio.sleep(delay)


    return delay
