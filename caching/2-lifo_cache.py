#!/usr/bin/env python3
'''LRU that inherits from BaseCashe'''


from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFO (Last-In, First-Out) caching system."""

    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.order = []  # List to track insertion order

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The value of the item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update order (not necessary for LIFO in this simple case)
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the last item added
            last_key = self.order.pop(0)  # LIFO: Remove from the beginning
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item.

        Returns:
            The value of the item if found, None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]