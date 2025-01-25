#!/usr/bin/env python3
'''MRU Cach that inherits from BashCaching'''

class BaseCaching:
    """
    BaseCaching is a base class for caching systems.
    It initializes the cache data and sets a maximum number of items allowed in the cache.
    """
    MAX_ITEMS = 4  # Maximum number of items allowed in the cache

    def __init__(self):
        """
        Initializes the cache data as an empty dictionary.
        This will be used to store the cached items.
        """
        self.cache_data = {}  # Dictionary to store cache data


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching and implements the Most Recently Used (MRU)
    eviction policy. If the cache exceeds the MAX_ITEMS limit, it discards the most recently used item.
    """

    def __init__(self):
        """
        Initializes the MRUCache.
        Calls the parent class (BaseCaching) constructor to set up the cache_data dictionary.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache with the given key.

        If the cache exceeds the MAX_ITEMS limit, it evicts the most recently used (MRU) item.

        Args:
            key (str): The key to associate with the item.
            item (str): The item to store in the cache.

        If key or item is None, this method does nothing.

        If the number of items in the cache exceeds MAX_ITEMS, the most recently added item will be discarded.
        The key of the discarded item will be printed in the format: "DISCARD: <key>"
        """
        # If key or item is None, do nothing
        if key is None or item is None:
            return
        
        # Insert the item into the cache
        self.cache_data[key] = item
        
        # Check if the number of items exceeds the maximum allowed
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
