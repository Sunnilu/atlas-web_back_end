'''LIFOCache that inherits from BaseCaching'''


from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that uses the LIFO (Last In, First Out)
    algorithm to manage cache eviction. When the cache exceeds MAX_ITEMS,
    the last item inserted is discarded.
    """
    
    def __init__(self):
        """Initialize LIFOCache instance."""
        super().__init__()

    def put(self, key, item):
        """
        Assigns the given item to the cache with the specified key.
        
        If either key or item is None, the method does nothing.
        If the number of items exceeds MAX_ITEMS, the most recent item
        inserted is discarded following the LIFO algorithm.

        Arguments:
            key (str): The key to store the item.
            item (any): The item to store in the cache.
        """
        if key and item:
            self.cache_data[key] = item
            
            # Check if the cache exceeds the maximum allowed items
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the last inserted key and discard it (LIFO eviction)
                last_key = next(reversed(self.cache_data))  # Get the last inserted key
                discarded_item = self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")

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
        return self.cache_data[key]