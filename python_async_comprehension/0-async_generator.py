#!/usr/bin/env python3
"""Async-Generator that takes no arguments"""


import asyncio
import random
from typing import Generator


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.randint(0, 10)  # Yield a random number between 0 and 10


async def main():
    async for value in async_generator():
        print(value)


# Run the main function to see the output
if __name__ == "__main__":
    asyncio.run(main())
