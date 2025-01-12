#!/usr/bin/env python3
"""change wait_n adjust to wait_random"""


import asyncio
import random

# Same wait_random function
async def wait_random(max_delay: int) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# New task_wait_random function that returns a Task
async def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))

# Altered wait_n function to use task_wait_random
async def task_wait_n(n: int, max_delay: int):
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    # Gather the results once all tasks are done
    delays = await asyncio.gather(*tasks)
    return delays



