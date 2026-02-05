# Representation Analysis

From the experiments, it’s clear that adjacency lists handle large graphs much better.
Matrix memory grows with V², so it gets big very fast.
By 10,000 nodes it was already using hundreds of MB, and near 100,000 nodes it would need tens of GB, which just isn’t realistic for most computers.

Adjacency lists only store edges that actually exist, so they save a lot of memory on sparse graphs.
They also worked better with Dijkstra’s since the algorithm only loops through real neighbors instead of checking every possible node.

Matrices still have a use when graphs are dense and you need fast edge lookups, but for most real-world networks like roads or social graphs, lists make more sense.