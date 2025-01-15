#!/usr/bin/env python3
'''MRUCache that inherits from BaseCaching'''


from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that uses the Most Recently Used (MRU) algorithm
    to manage cache eviction. When the cache exceeds MAX_ITEMS, the most recently
    used item is discarded.
    """

    def __init__(self):
        """Initialize MRUCache instance."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache. If the cache exceeds MAX_ITEMS, the most
        recently used item is discarded.
        
        Arguments:
            key (str): The key to store the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return
        
        # If the key is already in the cache, we update it
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        
        # Add the new item to the cache
        self.cache_data[key] = item
        
        # Check if the cache exceeds the maximum allowed items
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the most recently used item
            discarded_key, discarded_item = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieves the item associated with the specified key from the cache.
        
        Arguments:
            key (str): The key to look up in the cache.
        
        Returns:
            The item associated with the key, or None if the key doesn't exist
            or if the key is None.
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Move the accessed item to the end (mark as most recently used)
        self.cache_data.move_to_end(key)
        return self.cache_data[key]