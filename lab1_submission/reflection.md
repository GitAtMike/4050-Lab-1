# Reflection

One thing that surprised me was how quickly matrix memory usage exploded.
I expected it to be larger than lists, but seeing it reach hundreds of MB and then require over 70GB really put it into perspective.
I'm glad that my OS killed it immediately so it didn't harm the PC.

It was also interesting that matrix lookups weren’t massively faster, but Dijkstra’s became much slower with a matrix.
That showed me that iterating neighbors is a bigger factor than just checking if an edge exists.

Overall, this lab made the tradeoffs very clear and helped me understand why adjacency lists are usually preferred for large sparse graphs.
