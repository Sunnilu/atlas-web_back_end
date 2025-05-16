#!/usr/bin/env python3
"""LRUCache class implementing LRU cache algorithm."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache implementation."""

    def __init__(self):
        """Initialize class instance."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """Add an item in the cache, discarding least recently used if full."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys_order.remove(key)

        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.keys_order.pop(0)
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """Retrieve an item from the cache by key, updating recent usage."""
        if key in self.cache_data:
            self.keys_order.remove(key)
            self.keys_order.append(key)
            return self.cache_data[key]
        return None
