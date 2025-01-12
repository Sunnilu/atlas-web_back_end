#!/usr/bin/env python3
import asyncio
from typing import List  # Import List from typing for type annotations

# Assuming async_generator is imported
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''
    Collects 10 random numbers using an async comprehension over async_generator.
    
    Returns:
        List[float]: A list of 10 random numbers (floats) yielded by async_generator.
    '''
    try:
        # Use async comprehension to collect 10 random numbers
        result = [i async for i in async_generator()][:10]
        return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

