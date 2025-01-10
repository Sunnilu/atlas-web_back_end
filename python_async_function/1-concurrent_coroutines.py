#!/usr/bin/env python3
"""An async routine called wait_n that takes in 2 int arguments."""


import asyncio
import random  # Import the random module
from typing import List

async def wait_random(max_delay: int) -> float:
    """Simulate a random delay and return the delay."""
    delay = random.uniform(0, max_delay)  # random.uniform requires random to be imported
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` n times with the specified max_delay.
    Returns a list of delays (float values) in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of tasks that each call wait_random with max_delay
    tasks: List[asyncio.Future] = [wait_random(max_delay) for _ in range(n)]
    
    # Gather the results of all tasks (i.e., the delays)
    delays: List[float] = await asyncio.gather(*tasks)
    
    # Return the list of delay
    
    return delays

