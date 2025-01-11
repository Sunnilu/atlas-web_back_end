#!/usr/bin/env python3
"""async_comprehension over async_generator."""


import asyncio
import random
from typing import List


async def async_generator() -> Generator[int, None, None]:
    """
    Asynchronous generator that yields a random integer between 0 and 10,
    one value per second, for 10 iterations.

    Yields:
        int: A random integer between 0 and 10.

    Returns:
        None: This generator does not return any value when exhausted.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.randint(0, 10)  # Yield a random integer between 0 and 10


async def async_comprehension() -> List[int]:
    """
    Asynchronously collects 10 random integers from the async_generator
    using an async comprehension and returns them as a list.

    Returns:
        List[int]: A list of 10 random integers collected from async_generator.
    """
    return [num async for num in async_generator()]


async def main():
    """
    Runs the async_comprehension coroutine and prints the collected random
    integers.
    """
    random_numbers = await async_comprehension()
    print(random_numbers)


# Run the main function to see the output
if __name__ == "__main__":
    asyncio.run(main())



