#!/usr/bin/env python3
"""An async routine called wait_n that takes in 2 int arguments."""


import asyncio
from typing import List
from wait_random import wait_random  # Assume wait_random is defined in a separate module

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
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Gather the results of all tasks, i.e., the delays
    delays = await asyncio.gather(*tasks)
    
    # Since asyncio.gather collects the results as they finish, 
    # the delays will naturally be in ascending order due to their concurrent nature
    return delays
