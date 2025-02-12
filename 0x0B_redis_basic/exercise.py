#!/usr/bin/env python3
'''Provide a cache class with method call counting'''

import redis
import uuid
import functools
from typing import Union, Callable, Optional

def count_calls(method: Callable) -> Callable:
    """A decorator to count how many times a method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Get the qualified name of the method (e.g., 'Cache.store')
        key = method.__qualname__
        
        # Increment the count in Redis by 1 for this key
        self._redis.incr(key)
        
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    
    return wrapper

class Cache:
    def __init__(self):
        """Initialize the Cache instance and Redis connection."""
        try:
            self._redis = redis.Redis()
            # Ensure Redis is available
            if not self._redis.ping():
                raise ConnectionError("Unable to connect to Redis server.")
            # Flush the Redis database to clear any existing data
            self._redis.flushdb()
            print("Redis database flushed and connection is successful.")
        except redis.RedisError as e:
            raise ConnectionError(f"Redis connection error: {e}")

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis under a random key."""
        # Ensure that the data type is valid
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, int, bytes, float]]:
        """Retrieve data from Redis and apply a conversion function if provided."""
        data = self._redis.get(key)
        
        # If no data is found, return None (default Redis behavior)
        if data is None:
            return None
        
        # Apply the conversion function if provided
        if fn:
            return fn(data)
        
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as an integer."""
        return self.get(key, fn=int)

    def get_call_count(self, method_name: str) -> int:
        """Retrieve the call count for a specific method."""
        key = method_name
        count = self._redis.get(key)
        if count is None:
            return 0
        return int(count)


# Example usage of the Cache class
if __name__ == "__main__":
    try:
        cache = Cache()
        key = cache.store("my data")  # Store some string data
        print(f"Stored data under key: {key}")
        
        key2 = cache.store(123)  # Store integer data
        print(f"Stored data under key: {key2}")

        # Test the count_calls decorator by storing data multiple times
        for _ in range(5):
            cache.store("test data")
        
        # Check the number of times the store method was called
        store_call_count = cache.get_call_count("Cache.store")
        print(f"The store method was called {store_call_count} times.")

    except Exception as e:
        print(f"Error: {e}")
