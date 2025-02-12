#!/usr/bin/env python3
'''Provide a cache class'''

import redis
import uuid
from typing import Union

class Cache:
    def __init__(self):
        # Initialize Redis client and ensure it's connected
        try:
            self._redis = redis.Redis()
            # Check connection to Redis server
            if not self._redis.ping():
                raise ConnectionError("Unable to connect to Redis server.")
            # Flush the Redis database to clear any existing data
            self._redis.flushdb()
            print("Redis database flushed and connection is successful.")
        except redis.RedisError as e:
            raise ConnectionError(f"Redis connection error: {e}")

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Ensure that the data type is valid and log it
        if not isinstance(data, (str, bytes, int, float)):
            raise TypeError(f"Unsupported data type: {type(data)}")
        
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        try:
            # Store the data in Redis under the generated key
            self._redis.set(key, data)
            print(f"Data stored under key: {key}")
        except redis.RedisError as e:
            raise ConnectionError(f"Error storing data in Redis: {e}")
        
        # Return the generated key
        return key


# Example usage of the Cache class
if __name__ == "__main__":
    try:
        cache = Cache()
        key = cache.store("my data")  # Store some string data
        print(f"Stored data under key: {key}")

        key2 = cache.store(123)  # Store integer data
        print(f"Stored data under key: {key2}")
    except Exception as e:
        print(f"Error: {e}")
