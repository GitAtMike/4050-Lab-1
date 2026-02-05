# Representation Analysis

Based on the experiments so far, adjacency lists and adjacency matrices each have strengths depending on the situation.

Adjacency lists are more memory efficient, especially as the number of nodes increases. The experiments showed that matrix memory grows very quickly with graph size, becoming impractical around tens of thousands of nodes. Lists only store existing edges, so they scale much better for sparse graphs.

Adjacency matrices are faster for checking if a specific edge exists because they use direct indexing (O(1) lookup). The benchmarks showed matrix edge queries were sometimes faster than lists. However, this speed advantage is small compared to the large memory cost.

Overall, adjacency lists are better for large sparse graphs, while adjacency matrices are more suitable for small or dense graphs where fast edge lookup is important.
