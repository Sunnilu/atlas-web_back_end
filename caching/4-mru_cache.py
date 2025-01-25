#!/usr/bin/env python3
'''MRUCache that inherits from BaseCaching'''


class MRUCache(BaseCaching):
    """
    A caching system implementing the Most Recently Used (MRU) eviction policy.

    Attributes:
    cache_data (dict): Dictionary storing cached items (inherited from BaseCaching)
    MAX_ITEMS (int): Maximum number of items allowed in the cache (from BaseCaching)

    Methods:
    put(key, item): Adds an item to the cache, evicting the most recently used item if full
    get(key): Retrieves an item from the cache, moving it to the front
    """

    def __init__(self):
        """
        Initializes the MRUCache instance, calling the parent class constructor.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
        key: Cache key
        item: Item to store

        Notes:
        - Does nothing if key or item is None
        - Evicts the most recently used item if cache is full
        """
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = max(self.cache_data.keys(), key=self.cache_data.get)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
        key: Cache key

        Returns:
        Cached item if exists, otherwise None

        Notes:
        Moves retrieved item to the front of the cache
        """
        if key is None or key not in self.cache_data:
            return None
        
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value



