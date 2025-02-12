cache = Cache()
key = cache.store("my data")  # Store some string data
print(f"Stored data under key: {key}")

key2 = cache.store(123)  # Store integer data
print(f"Stored data under key: {key2}")
