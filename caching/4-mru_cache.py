#!/usr/bin/env python3

class BaseCaching:
    """
    BaseCaching is a base class for caching systems.
    Initializes cache_data and sets the maximum number of items allowed.
    """
    MAX_ITEMS = 4  # Maximum number of items allowed in the cache

    def __init__(self):
        """
        Initializes cache_data as an empty dictionary to store cached items.
        """
        self.cache_data = {}  # This will store the cached items


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that uses the Most Recently Used (MRU) eviction policy.
    In this policy, when the cache exceeds the maximum number of items (MAX_ITEMS),
    the most recently used item is discarded.
    """

    def __init__(self):
        """
        Initializes MRUCache. Calls the parent class constructor to initialize cache_data.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a new item to the cache with the given key.

        If the number of items exceeds MAX_ITEMS, evicts the most recently used item.

        Args:
            key (str): The key for the item.
            item (str): The item to store in the cache.

        If key or item is None, the method does nothing.
        """
        if key is None or item is None:
            return
        
        # Insert the item into the cache
        self.cache_data[key] = item
        
        # Check if the cache exceeds the maximum number of items
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # The most recently added item is the last one in the dictionary
            mru_key = list(self.cache_data.keys())[-1]
            
            # Discard the most recently added item
            self.cache_data.pop(mru_key)
            
            # Print the discarded key
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key (str): The key for which the value is to be retrieved.

        Returns:
            str or None: The value associated with the key, or None if the key does not exist.
        """
        return self.cache_data.get(key, None)

    def print_cache(self):
        """
        Prints the current state of the cache.

        This method displays the cache in the following format:
        Current cache:
        A: Hello
        B: World
        C: Holberton
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")

