#!/usr/bin/env python3

class BaseCaching:
    """
    BaseCaching is a base class for caching systems.
    It initializes the cache_data dictionary and sets the maximum allowed cache size.
    """
    MAX_ITEMS = 4  # Maximum number of items allowed in the cache

    def __init__(self):
        """
        Initializes the cache_data dictionary to store the cached items.
        """
        self.cache_data = {}  # Dictionary to store cache items


class MRUCache(BaseCaching):
    """
    MRUCache is a class that implements the Most Recently Used (MRU) eviction policy.
    When the cache exceeds the maximum size, it discards the most recently used item.
    This class inherits from the BaseCaching class.
    """

    def __init__(self):
        """
        Initializes the MRUCache and calls the parent class constructor to initialize cache_data.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache with the given key.

        If the cache exceeds MAX_ITEMS, it evicts the most recently used item.

        Args:
            key (str): The key to associate with the item.
            item (str): The item to store in the cache.

        If key or item is None, the method does nothing.
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
            discarded_item = self.cache_data.pop(mru_key)
            
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
        # Return the value associated with the key, or None if the key is not in the cache
        return self.cache_data.get(key, None)
