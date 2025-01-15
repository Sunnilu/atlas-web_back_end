#!/usr/bin/env python3
'''BasicCache that inherits from BaseCaching'''


from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def __init__(self):
        """Initialize BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Assign item to the cache with key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return the item associated with the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
