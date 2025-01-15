#!/usr/bin/env python3
'''BasicCache that inherits from BaseCaching'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a simple caching system that inherits from BaseCaching.
    This class does not have any limit on the number of items stored.
    
    Methods:
        put(key, item):
            Stores the item in the cache associated with the given key.
            If either the key or the item is None, nothing is stored.
        
        get(key):
            Retrieves the item associated with the given key from the cache.
            Returns None if the key does not exist or if the key is None.
    """
    
    def __init__(self):
        """Initialize the BasicCache instance."""
        super().__init__()

    def put(self, key, item):
        """
        Assigns the given item to the cache with the specified key.

        Arguments:
            key (str): The key to associate with the item.
            item (any): The item to store in the cache.

        If either the key or item is None, this method does nothing.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item associated with the specified key from the cache.

        Arguments:
            key (str): The key to look up in the cache.

        Returns:
            The item associated with the key, or None if the key is not found
            or if the key is None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
