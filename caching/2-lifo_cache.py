#!/usr/bin/env python3
'''LRU that inherits from BaseCashe'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that uses the Last-In-First-Out (LIFO) eviction policy.
    This means that when the cache exceeds the maximum number of allowed items, the most recently added item
    will be discarded.

    Inherits from the BaseCaching class, which provides the cache_data dictionary to store cached items
    and the MAX_ITEMS constant to control the maximum number of items allowed in the cache.

    Attributes:
        cache_data (dict): A dictionary to store the cached items.
        MAX_ITEMS (int): The maximum number of items allowed in the cache, inherited from BaseCaching.
    """
    
    def __init__(self):
        """
        Initialize the LIFOCache object.

        Calls the parent class's __init__ method to initialize the cache_data dictionary and MAX_ITEMS constant.

        Args:
            None
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache with the provided key.
        
        If the number of items in the cache exceeds the maximum allowed (MAX_ITEMS), 
        the most recently added item is discarded following the LIFO eviction policy.

        Args:
            key (str): The key associated with the item to be cached.
            item (any): The item to be stored in the cache.
            
        Returns:
            None
            
        Side Effects:
            - If the cache exceeds the MAX_ITEMS limit, the last added item is evicted.
            - If either the `key` or `item` is None, no action is taken.
            - If eviction occurs, a message "DISCARD: key" is printed.
        """
        # If key or item is None, do nothing
        if key is None or item is None:
            return
        
        # Store the item in cache_data with the provided key
        self.cache_data[key] = item
        
        # If the cache exceeds MAX_ITEMS, evict the last inserted item (LIFO eviction)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the last inserted key (LIFO eviction)
            last_key = next(reversed(self.cache_data))  # Retrieves the last inserted key
            del self.cache_data[last_key]  # Remove the last inserted item from the cache
            print(f"DISCARD: {last_key}")  # Print the evicted key

    def get(self, key):
        """
        Retrieve an item from the cache by its key.

        If the key is None or does not exist in the cache, return None.

        Args:
            key (str): The key of the item to retrieve from the cache.

        Returns:
            The item associated with the key if it exists, otherwise None.

        Side Effects:
            None
        """
        # Return None if the key is None or the key doesn't exist in the cache
        if key is None or key not in self.cache_data:
            return None
        
        # Return the item associated with the given key
        return self.cache_data[key]
