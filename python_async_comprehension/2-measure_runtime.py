#!/usr/bin/env python3
"""write a measure_runtime coroutine execute async_comprehension four times in parallel"""


import asyncio
import random
import time
from typing import List


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random integer between 0 and 10,
    one value per second, for 10 iterations.

    Yields:
        float: A random number between 0 and 10.

    Returns:
        None: This generator does not return any value when exhausted.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.randint(0, 10)  # Yield a random integer between 0 and 10


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random integers from the async_generator 
    using an async comprehension and returns them as a list.

    This coroutine demonstrates the usage of async comprehension to 
    gather values from the async_generator and accumulate them in a list.

    Returns:
        List[float]: A list of 10 random numbers collected from async_generator.
    """
    return [float(num) async for num in async_generator()]


async def measure_runtime() -> float:
    """
    Executes the async_comprehension coroutine four times in parallel using 
    asyncio.gather, and measures the total runtime.

    This function demonstrates how to measure the total runtime of 
    asynchronous tasks running concurrently.

    Returns:
        float: The total runtime for executing the four async_comprehension 
               coroutines concurrently.
    """
    start_time = time.time()  # Start measuring time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()  # End measuring time
    return end_time - start_time  # Return the total runtime


async def main():
    """
    Runs the measure_runtime coroutine and prints the total runtime of the 
    async_comprehension coroutines executed in parallel.

    This function demonstrates how to call measure_runtime and display the 
    result.
    """
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime:.2f} seconds")


# Run the main function to see the output
if __name__ == "__main__":
    asyncio.run(main())
