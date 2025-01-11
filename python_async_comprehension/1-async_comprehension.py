#!/usr/bin/env python3
"""async_comprehension over async_generator."""


import asyncio
import random
from typing import List


# Import async_generator from the previous task
async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random float between 0 and 10,
    one value per second, for 10 iterations.

    Yields:
        float: A random number between 0 and 10.

    Returns:
        None: This generator does not return any value when exhausted.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.randint(0, 10)  # Yield a random number between 0 and 10


# New coroutine async_comprehension
async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers from the async_generator 
    using an async comprehension and returns them as a list.

    Returns:
        List[float]: A list of 10 random numbers collected from async_generator.
    """
    return [num async for num in async_generator()]


async def main():
    """Runs the async_comprehension and prints the collected random numbers."""
    random_numbers = await async_comprehension()
    print(random_numbers)


# Run the main function to see the output
if __name__ == "__main__":
    asyncio.run(main())

