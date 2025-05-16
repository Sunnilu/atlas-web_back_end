#!/usr/bin/env python3
"""FIFOCache class implementing FIFO cache algorithm."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache implementation."""

    def __init__(self):
        """Initialize class instance."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """Add an item in the cache, discarding oldest if full."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.keys_order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.keys_order.pop(0)
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key, None)
