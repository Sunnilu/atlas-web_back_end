#!/usr/bin/env python3
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def call_history(method: Callable) -> Callable:
    """
    A decorator to store the history of inputs and outputs for a function.

    Each time the decorated method is called, this decorator stores the input 
    arguments in one list and the outputs in another list in Redis.

    Args:
        method (Callable): The method being decorated.

    Returns:
        Callable: The wrapped function.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores the inputs and outputs of the method.

        Args:
            self: The instance of the class (Cache).
            *args: Positional arguments to be passed to the original method.
            **kwargs: Keyword arguments (not used in this version).

        Returns:
            The result of the original method call.
        """
        # Get the qualified name of the method (e.g., 'Cache.store')
        key_inputs = f"{method.__qualname__}:inputs"
        key_outputs = f"{method.__qualname__}:outputs"
        
        # Store the inputs in Redis (string representation of args)
        self._redis.rpush(key_inputs, str(args))
        
        # Call the original method
        output = method(self, *args, **kwargs)
        
        # Store the output in Redis
        self._redis.rpush(key_outputs, str(output))
        
        return output

    return wrapper


class Cache:
    """
    A class representing a cache system using Redis to store data.
    It supports storing, retrieving, and keeping track of method call history.
    """

    def __init__(self):
        """
        Initialize the Cache instance and connect to the Redis server.

        Raises:
            ConnectionError: If the connection to the Redis server fails.
        """
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
        """
        Store data in Redis under a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.

        Raises:
            TypeError: If the data type is not one of str, bytes, int, or float.
            ConnectionError: If storing data in Redis fails.
        """
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
        """
        Retrieve data from Redis and apply a conversion function if provided.

        Args:
            key (str): The key to retrieve data for.
            fn (Optional[Callable]): A function to convert the data to the desired format.

        Returns:
            Optional[Union[str, int, bytes, float]]: The converted data, or None if the key does not exist.
        """
        data = self._redis.get(key)
        
        # If no data is found, return None (default Redis behavior)
        if data is None:
            return None
        
        # Apply the conversion function if provided
        if fn:
            return fn(data)
        
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis as a string.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[str]: The data as a string, or None if not found.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis as an integer.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[int]: The data as an integer, or None if not found.
        """
        return self.get(key, fn=int)

    def get_call_count(self, method_name: str) -> int:
        """
        Retrieve the call count for a specific method.

        Args:
            method_name (str): The name of the method (e.g., 'Cache.store').

        Returns:
            int: The number of times the method has been called.
        """
        key = method_name
        count = self._redis.get(key)
        if count is None:
            return 0
        return int(count)

    def replay(self, method: Callable):
        """
        Replay the call history for a specific method.

        This function will display how many times the method was called, along 
        with the inputs and outputs for each call.

        Args:
            method (Callable): The method to replay the call history for.
        """
        key_inputs = f"{method.__qualname__}:inputs"
        key_outputs = f"{method.__qualname__}:outputs"
        
        # Get the inputs and outputs history from Redis
        inputs = self._redis.lrange(key_inputs, 0, -1)
        outputs = self._redis.lrange(key_outputs, 0, -1)
        
        # Print the header
        print(f"{method.__qualname__} was called {len(inputs)} times:")
        
        # Loop over inputs and outputs and display them
        for input_data, output_data in zip(inputs, outputs):
            # Print the formatted call history
            print(f"{method.__qualname__}(*{eval(input_data)}) -> {output_data.decode('utf-8')}")


# Example usage of the Cache class
if __name__ == "__main__":
    try:
        # Initialize the cache
        cache = Cache()
        
        # Store some data
        key1 = cache.store("foo")
        key2 = cache.store("bar")
        key3 = cache.store(42)
        
        # Replay the call history for the store method
        cache.replay(cache.store)
    except Exception as e:
        print(f"Error: {e}")


