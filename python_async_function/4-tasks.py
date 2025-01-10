 #!/usr/bin/env python3
"""Asynchronous coroutine to spawn tasks using task_wait_random."""

import asyncio
from typing import List

#Take the code from wait_n and alter it into a new function task_wait_n.
wait_n = __import__('1-concurrent_coroutines').wait_n

# Import task_wait_random from the correct file
task_wait_random = __import__('1-concurrent_coroutines').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates n tasks for the task_wait_random coroutine and returns their results.

    Parameters:
    n (int): The number of tasks to run.
    max_delay (int): The maximum delay for each task.

    Returns:
    List[float]: A list of float values representing the delays.
    """
    # Create a list of tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Wait for all tasks to complete and gather the results
    results = await asyncio.gather(*tasks)
    
    return results

