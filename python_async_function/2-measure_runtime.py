#!/usr/bin/env python3
"""measure_time function with integers n and max_delay as arguments that measures the total execution time."""


import asyncio
import time
from typing import List
from 1-concurrent_coroutines.py import wait_n  # Correct import from 1-concurrent_coroutines.py

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the execution time for wait_n(n, max_delay) and returns the average time per task.
    
    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each task.
        
    Returns:
        float: The average time per task.
    """
    # Start time
    start_time = time.time()
    
    # Run the wait_n function asynchronously
    asyncio.run(wait_n(n, max_delay))
    
    # End time
    end_time = time.time()
    
    # Calculate total time and average time per task
    total_time = end_time - start_time
    average_time = total_time / n
    
    return average_time
