#!/usr/bin/env python3
'''Provide a cache class'''

import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, int, bytes, float]]:
        # Retrieve the data from Redis
        data = self._redis.get(key)
        
        # If no data is found, return None (default Redis behavior)
        if data is None:
            return None
        
        # If a function is provided, apply it to the retrieved data
        if fn:
            # Special handling if we try to convert a byte to an int
            if fn == int:
                try:
                    # Attempt to decode byte data before converting to int if it's a valid number
                    decoded_data = data.decode("utf-8")
                    return int(decoded_data)  # Convert string number to integer
                except (ValueError, UnicodeDecodeError):
                    # If decoding or conversion fails, raise a clear error
                    raise ValueError(f"Cannot convert data to int: {data}")
            
            # If function is not int, just apply the function normally
            return fn(data)
        
        # If no function is provided, return the data as it is
        return data

    def get_str(self, key: str) -> Optional[str]:
        # A method to retrieve the data as a string
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        # A method to retrieve the data as an integer
        return self.get(key, fn=int)


# Example usage of the Cache class
if __name__ == "__main__":
    try:
        cache = Cache()
        key = cache.store("my data")  # Store some string data
        print(f"Stored data under key: {key}")

        key2 = cache.store(123)  # Store integer data
        print(f"Stored data under key: {key2}")

        # Test the get_str and get_int methods
        print(f"Retrieved string: {cache.get_str(key)}")
        print(f"Retrieved integer: {cache.get_int(key2)}")

        # Additional test cases to ensure everything works correctly
        TEST_CASES = {
            b"foo": None,  # No conversion function
            123: int,      # Convert to integer
            "bar": lambda d: d.decode("utf-8")  # Decode bytes to string
        }

        # Run the test cases
        for value, fn in TEST_CASES.items():
            stored_key = cache.store(value)
            result = cache.get(stored_key, fn=fn)
            assert result == value, f"Expected {value}, but got {result}"
            print(f"Test passed for value: {value}")
    
    except Exception as e:
        print(f"Error: {e}")
