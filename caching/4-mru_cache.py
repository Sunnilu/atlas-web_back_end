#!/usr/bin/env python3
""" 
4-mru_cache module
This module defines the MRUCache class, which inherits from BaseCaching.
The MRUCache class implements a caching system that uses the Most Recently Used (MRU) eviction policy.
When the cache exceeds the maximum allowed size, it discards the most recently used item.
"""

class BaseCaching:
    """
    BaseCaching is a base class for caching systems.
    It initializes the cache_data dictionary and sets the maximum allowed number of items.
    """
    MAX_ITEMS = 4  # Default maximum number of items allowed in the cache

    def __init__(self):
        """
        Initializes the cache_data as an empty dictionary.
        """
        self.cache_data = {}

class MRUCache(BaseCaching):
    """
    MRUCache is a class that implements the Most Recently Used (MRU) eviction policy.
    If the cache exceeds the maximum number of items, the most recently used item is discarded.
    """
    
    def __init__(self):
        """
        Initializes the MRUCache and calls the parent class constructor to set up the cache_data.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a new item to the cache with the given key.
        If the cache exceeds MAX_ITEMS, it evicts the most recently used item.

        If either the key or item is None, the method does nothing.

        Args:
            key (str): The key for the item.
            item (str): The item to store in the cache.
        """
        # If key or item is None, do nothing
        if key is None or item is None:
            return
        
        # Insert the item into the cache
        self.cache_data[key] = item
        
        # If the cache exceeds the maximum number of items, evict the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the most recently added key (the last key in the dictionary)
            mru_key = list(self.cache_data.keys())[-1]
            
            # Discard the most recently added item
            self.cache_data.pop(mru_key)
            
            # Print the discarded key
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.
        
        If the key is None or doesn't exist in the cache, returns None.

        Args:
            key (str): The key for which the value is to be retrieved.

        Returns:
            str or None: The value associated with the key, or None if the key does not exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

    def print_cache(self):
        """
        Prints the current state of the cache in the following format:
        Current cache:
        A: Hello
        B: World
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")


