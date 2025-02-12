#!/usr/bin/env python3
'''Provide a cache class'''

import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        # Initialize Redis client
        self._redis = redis.Redis()
        # Flush the Redis database to clear any existing data
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the data in Redis under the generated key
        self._redis.set(key, data)
        # Return the generated key
        return key


# Example usage of the Cache class
cache = Cache()
key = cache.store("my data")  # Store some string data
print(f"Stored data under key: {key}")

key2 = cache.store(123)  # Store integer data
print(f"Stored data under key: {key2}")
