#!/usr/bin/env python3
"""
4-mru_cache module.
This module defines the MRUCache class, which is a subclass of BaseCaching.
It implements the Most Recently Used (MRU) eviction policy for caching.
"""

class BaseCaching:
    """
    BaseCaching is a base class for caching systems.

    Attributes:
        MAX_ITEMS (int): Maximum number of items allowed in the cache.
        cache_data (dict): Dictionary to store cached items.
    """
    MAX_ITEMS = 4  # Default maximum number of items in the cache

    def __init__(self):
        """
        Initializes the cache_data as an empty dictionary.
        """
        self.cache_data = {}  # Dictionary to store the cached items


class MRUCache(BaseCaching):
    """
    MRUCache class that implements the Most Recently Used (MRU) eviction policy.

    In this policy, when the cache exceeds the maximum allowed number of items (MAX_ITEMS),
    the most recently used item is discarded.
    """

    def __init__(self):
        """
        Initializes the MRUCache. Calls the parent class constructor to initialize cache_data.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache with the given key.

        If the number of items exceeds MAX_ITEMS, it evicts the most recently used item.

        Args:
            key (str): The key to associate with the item.
            item (str): The item to store in the cache.

        If key or item is None, the method does nothing.
        """
        if key is None or item is None:
            return
        
        # Insert or update the item in the cache
        self.cache_data[key] = item
        
        # If the cache exceeds MAX_ITEMS, evict the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the most recently added key (the last one in the dictionary)
            mru_key = list(self.cache_data.keys())[-1]
            
            # Remove and discard the most recently added item
            self.cache_data.pop(mru_key)
            
            # Print the discarded key
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            str or None: The value associated with the key, or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data.get(key)

    def print_cache(self):
        """
        Prints the current state of the cache in the format:
        Current cache:
        A: Hello
        B: World
        C: Holberton
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")


