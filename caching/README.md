In computing, cache replacement policies (also known as cache replacement algorithms or cache algorithms) are optimizing instructions or algorithms which a computer program or hardware-maintained structure can utilize to manage a cache of information. Caching improves performance by keeping recent or often-used data items in memory locations which are faster, or computationally cheaper to access, than normal memory stores. When the cache is full, the algorithm must choose which items to discard to make room for new data.

The average memory reference time is[1]

T
=
m
×
T
m
+
T
h
+
E
{\displaystyle T=m\times T_{m}+T_{h}+E}
where

m
{\displaystyle m} = miss ratio = 1 - (hit ratio)
T
m
{\displaystyle T_{m}} = time to make main-memory access when there is a miss (or, with a multi-level cache, average memory reference time for the next-lower cache)
T
h
{\displaystyle T_{h}}= latency: time to reference the cache (should be the same for hits and misses)
E
{\displaystyle E} = secondary effects, such as queuing effects in multiprocessor systems

The hit ratio of a cache describes how often a searched-for item is found.

Hit-rate measurements are typically performed on benchmark applications, and the hit ratio varies by application. Video and audio streaming applications often have a hit ratio near zero, because each bit of data in the stream is read once (a compulsory miss), used, and then never read or written again. Many cache algorithms (particularly LRU) allow streaming data to fill the cache, pushing out information which will soon be used again (cache pollution).[2] Other factors may be size, length of time to obtain, and expiration. Depending on cache size, no further caching algorithm to discard items may be needed. Algorithms also maintain cache coherence when several caches are used for the same data, such as multiple database servers updating a shared data file.

First in first out (FIFO)
With this algorithm, the cache behaves like a FIFO queue; it evicts blocks in the order in which they were added, regardless of how often or how many times they were accessed before.

Last in first out (LIFO) or First in last out (FILO)
The cache behaves like a stack, and unlike a FIFO queue. The cache evicts the block added most recently first, regardless of how often or how many times it was accessed before.

Least Recently Used (LRU)
Discards least recently used items first. This algorithm requires keeping track of what was used and when, which is cumbersome. It requires "age bits" for cache lines, and tracks the least recently used cache line based on these age bits. When a cache line is used, the age of the other cache lines changes.