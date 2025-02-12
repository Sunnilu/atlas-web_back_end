#!/usr/bin/env python3
'''Cache system with method call tracking and input/output history.'''

import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    '''Decorator to count how many times a method is called.'''
    
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrap method to increment its call count in Redis.'''
        key = method.__qualname__
        self._redis.incr(key)  # Increment the call count in Redis
        return method(self, *args, **kwargs)
    
    return wrapper


def call_history(method: Callable) -> Callable:
    '''Decorator to record method input/output in Redis.'''

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Record inputs and outputs for the method in Redis.'''
        key = method.__qualname__
        # Store input arguments in Redis
        self._redis.rpush(f"{key}:inputs", str(args))
        
        # Execute the method and store its output
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(output))
        
        return output
    
    return wrapper


def replay(method: Callable) -> None:
    '''Replay the history of calls to a method from Redis.'''

    key = method.__qualname__
    inputs = self._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = self._redis.lrange(f"{key}:outputs", 0, -1)
    
    print(f"{key} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{key}(*{input_data.decode()}) -> {output_data.decode()}")


class Cache:
    '''Cache class that interacts with Redis to store data and track method calls.'''

    def __init__(self) -> None:
        '''Initialize the Redis connection and flush the database.'''
        try:
            self._redis = redis.Redis()
            if not self._redis.ping():
                raise ConnectionError("Unable to connect to Redis server.")
            self._redis.flushdb()
            print("Redis database flushed and connection is successful.")
        except redis.RedisError as e:
            raise ConnectionError(f"Redis connection error: {e}")
    
    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store data in Redis under a unique key and return the key.'''
        if not isinstance(data, (str, bytes, int, float)):
            raise TypeError(f"Unsupported data type: {type(data)}")

        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        print(f"Data stored under key: {key}")
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, int, bytes, float]]:
        '''Retrieve data from Redis and optionally convert it using the provided function.'''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        '''Retrieve data from Redis and decode it as a string.'''
        return self.get(key, fn=lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        '''Retrieve data from Redis and convert it to an integer.'''
        return self.get(key, fn=int)
    
    def get_call_count(self, method_name: str) -> int:
        '''Retrieve the call count for a particular method from Redis.'''
        count = self._redis.get(method_name)
        return int(count) if count else 0

