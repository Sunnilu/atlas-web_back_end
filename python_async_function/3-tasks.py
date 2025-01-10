#!/usr/bin/env python3
"""Import and wrap the wait_random coroutine into an asyncio Task."""

import asyncio

# Dynamically import the wait_random function from 0-basic_async_syntax.py
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an task_wait_random integer max_delay returns asyncio.Task.

    Parameters:
    max_delay (int): The maximum delay time.

    Returns:
    asyncio.Task: A Task that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
