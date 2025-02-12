#!/usr/bin/env python3
import redis
import uuid
import functools
from typing import Union, Callable, Optional

def call_history(method: Callable) -> Callable:
    """A decorator to store the history of inputs and outputs of the function."""
    
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Get the qualified name of the method (e.g., 'Cache.store')
        key_inputs = f"{method.__qualname__}:inputs"
        key_outputs = f"{method.__qualname__}:outputs"
        
        # Store the inputs in Redis by appending the string representation of args
        self._redis.rpush(key_inputs, str(args))
        
        # Call the original method
        output = method(self, *args, **kwargs)
        
        # Store the output in Redis
        self._redis.rpush(key_outputs, str(output))
        
        # Return the output of the original function
        return output
    
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

    @call_history
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
        
        # Store some string data
        key = cache.store("my data")
        print(f"Stored data under key: {key}")
        
        # Store integer data
        key2 = cache.store(123)
        print(f"Stored data under key: {key2}")
        
        # Test call history decorator by storing data multiple times
        for _ in range(3):
            cache.store("test data")
        
        # Retrieve the call history for store method inputs and outputs
        key_inputs = f"Cache.store:inputs"
        key_outputs = f"Cache.store:outputs"
        
        # Retrieve and print inputs and outputs
        inputs = cache._redis.lrange(key_inputs, 0, -1)
        outputs = cache._redis.lrange(key_outputs, 0, -1)
        
        print(f"Inputs: {inputs}")
        print(f"Outputs: {outputs}")

    except Exception as e:
        print(f"Error: {e}")
