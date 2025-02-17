Redis stands for Remote Dictionary Service.

“You mean, like a Python dictionary?” you may ask.

Yes. Broadly speaking, there are many parallels you can draw between a Python dictionary (or generic hash table) and what Redis is and does:

A Redis database holds key:value pairs and supports commands such as GET, SET, and DEL, as well as several hundred additional commands.

Redis keys are always strings.

Redis values may be a number of different data types. We’ll cover some of the more essential value data types in this tutorial: string, list, hashes, and sets. Some advanced types include geospatial items and the new stream type.

Many Redis commands operate in constant O(1) time, just like retrieving a value from a Python dict or any hash table.

Redis creator Salvatore Sanfilippo would probably not love the comparison of a Redis database to a plain-vanilla Python dict. He calls the project a “data structure server” (rather than a key-value store, such as memcached) because, to its credit, Redis supports storing additional types of key:value data types besides string:string. But for our purposes here, it’s a useful comparison if you’re familiar with Python’s dictionary object.

Let’s jump in and learn by example. Our first toy database (with ID 0) will be a mapping of country:capital city, where we use SET to set key-value pairs:
