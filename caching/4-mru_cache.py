#!/usr/bin/env python3
'''MRUCache that inherits from BaseCaching'''


from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRU (Most Recently Used) caching system."""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.mru_order = []  # List to track MRU order

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
            # Update MRU order
            self.mru_order.remove(key)
        self.mru_order.append(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the least recently used item
            lru_key = self.mru_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item

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

        # Update MRU order
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]

# --- Test Cases ---

def test_mru_cache(max_items, num_items):
    """
    Test the MRU cache with given max_items and number of items to add.

    Args:
        max_items: Maximum number of items allowed in the cache.
        num_items: Number of items to add to the cache.
    """
    BaseCaching.MAX_ITEMS = max_items
    my_cache = MRUCache()

    for i in range(num_items):
        my_cache.put(str(i), str(i))

# --- Run Tests ---

print("Test with BaseCaching.MAX_ITEMS = 2 and 10 items:")
test_mru_cache(2, 10)

print("\nTest with BaseCaching.MAX_ITEMS = 5 and 10 items:")
test_mru_cache(5, 10)


