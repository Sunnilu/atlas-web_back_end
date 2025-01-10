#!/usr/bin/env python3
"""measure_time function with integers n and max_delay as arguments that measures the total execution time."""


import asyncio
import time
from typing import List

# Dynamically import the wait_random function from 1-concurrent_coroutines.py
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the execution time for `wait_n(n, max_delay)` and returns the average time per task.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: The average time per task (in seconds).
    """
    # Record the start time
    start_time: float = time.time()

    # Run the wait_n function asynchronously
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time: float = time.time()

    # Calculate total time and average time per task
    total_time: float = end_time - start_time
    average_time: float = total_time / n

    return average_time
