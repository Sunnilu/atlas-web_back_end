#!/usr/bin/env python3
"""Async-Generator that takes no arguments"""


import asyncio
import random
from typing import Generator


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


async def main():
    """Runs the async generator and prints each yielded value."""
    async for value in async_generator():
        print(value)


# Run the main function to see the output
if __name__ == "__main__":
    asyncio.run(main())
