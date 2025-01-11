#!/usr/bin/env python3
'''
This module contains the async_comprehension coroutine, which collects 10 random
numbers using async_generator with an async comprehension.
'''


import asyncio

# Import async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    '''
    Collects 10 random numbers using an async comprehension over async_generator.
    
    Returns:
        list: A list of 10 random numbers yielded by async_generator.
    '''
    # Use async comprehension to collect 10 random numbers
    return [i async for i in async_generator()][:10]
