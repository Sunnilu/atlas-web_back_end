#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis to store
'''
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    '''
    Decorator that counts how many times a method is called using Redis.
    Imagine counting how many times you've ignored the news about rising
    sea levels. Redis does this for your method calls, one existential dread
    at a time.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        Wrapper function that increments the count each time
        the decorated method is called. Redis tracks it all like
        keeping tabs on how many ice caps we have left or how many times
        your pug asks for dinner.
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    Decorator to store the history of inputs and outputs for a method.
    Every time the method is called, the input is logged into one list,
    and the output into another. Like keeping track of all your thoughts,
    but in Redis, and they never fade away.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = method.__qualname__ + ":inputs"
        outputs_key = method.__qualname__ + ":outputs"

        # Store input arguments as a string in the Redis list
        self._redis.rpush(inputs_key, str(args))

        # Call the original method and store its output
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))

        return output

    return wrapper


def replay(method: Callable):
    '''
    Function to display the history of calls made to a particular method.
    Shows how many times the method was called, and replays the inputs and
    outputs from previous calls. Like revisiting your embarrassing past, one
    function call at a time, except now it's logged in Redis.
    '''
    redis_instance = method.__self__._redis
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    # Get the number of times the method was called
    call_count = redis_instance.get(method_name).decode("utf-8")

    print(f"{method_name} was called {call_count} times:")

    # Get the list of inputs and outputs
    inputs = redis_instance.lrange(inputs_key, 0, -1)
    outputs = redis_instance.lrange(outputs_key, 0, -1)

    # Loop through inputs and outputs together
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode("utf-8")
        output_str = output_data.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")


class Cache:
    '''
    Cache class for storing and retrieving data in Redis.
    It now tracks how many times its methods are called,
    stores a history of inputs and outputs, and can replay the history
    of method calls like a detailed audit of every little thing you've done.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        Basically wiping everything clean like deleting the record
        of all those carbon emissions, so we can pretend everything’s fine.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis with a unique key, count how many times
        this method has been called, and keep a history of inputs and outputs.
        Like storing away little pieces of hope and also remembering every
        time you've tried to, in case you need to revisit your optimism later.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis, possibly transforming it.
        Redis gives everything back in bytes, like handing you
        a confusing climate report. You’ll need to decode it if you
        want it to make sense.
        '''
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        '''
        Retrieve a string from Redis.
        Redis speaks in bytecode, but this translates it back into words.
        '''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve an integer from Redis.
        Converts the chaos into a number you can count on—hopefully.
        '''
        return self.get(key, int)
