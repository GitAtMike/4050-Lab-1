# Additional Challenge — Hybrid Graph Representation

## Goal
Create a hybrid graph that:
- uses adjacency lists for sparse areas
- uses matrix blocks for dense subgraphs
- chooses automatically based on local density

## Idea
I would always keep an adjacency list for the whole graph (this guarantees the graph works for any size).
On top of that, I would detect “dense clusters” of nodes and store those clusters in small adjacency matrices (blocks).
This avoids the V² memory blow-up of a full matrix while still getting fast edge lookup inside dense regions.

## When to use a matrix block
For a cluster of k nodes:
- max edges is k*(k-1)/2 (undirected) or k*(k-1) (directed)
- density = actual_edges / max_edges

If density > threshold (ex: 0.1 or 0.2), store that cluster as a matrix block.

## Data structures
- adj_list: dict[node] -> list[(neighbor, weight)]
- blocks: list of Block objects:
  - block.nodes: list of node ids
  - block.index: dict[node_id] -> 0..k-1
  - block.matrix: k x k array (weights or 0/None)

## Operations
### add_edge(u, v, w)
- always add to adj_list
- if u and v are inside the same block, also update that block’s matrix

### has_edge(u, v)
- if u and v are in the same dense block: check matrix[u][v] (O(1))
- otherwise: scan adj_list[u] (O(degree))

### get_neighbors(u)
- if u is in a block: neighbors from the adj_list (still best for iteration)
- (optional) for very dense blocks, neighbors could be generated from the matrix row

## Why this is useful
Most real graphs are sparse overall, but some parts can be dense (ex: small communities in social networks).
This hybrid approach keeps memory close to the list representation, while improving edge lookup speed inside dense clusters.