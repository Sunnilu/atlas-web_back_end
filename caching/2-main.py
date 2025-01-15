#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()


def test_lifo_cache():
    # Test 1: MAX_ITEMS = 1, add 5 items
    print("Test 1: MAX_ITEMS = 1, adding 5 items")
    cache = LIFOCache()
    BaseCaching.MAX_ITEMS = 1
    for i in range(1, 6):
        cache.put(str(i), f"Item {i}")
        cache.print_cache()
    print()

    # Test 2: MAX_ITEMS = 2, add 10 items
    print("Test 2: MAX_ITEMS = 2, adding 10 items")
    cache = LIFOCache()
    BaseCaching.MAX_ITEMS = 2
    for i in range(1, 11):
        cache.put(str(i), f"Item {i}")
        cache.print_cache()
    print()

    # Test 3: MAX_ITEMS = 5, add 10 items
    print("Test 3: MAX_ITEMS = 5, adding 10 items")
    cache = LIFOCache()
    BaseCaching.MAX_ITEMS = 5
    for i in range(1, 11):
        cache.put(str(i), f"Item {i}")
        cache.print_cache()

test_lifo_cache()