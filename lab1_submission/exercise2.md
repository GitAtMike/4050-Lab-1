# Exercise 2 - Edge Query Benchmark

## Edge Lookup Results

| Size   | List Edge Q/s | Matrix Edge Q/s | Speedup |
| ------ | ------------- | --------------- | ------- |
| tiny   | 4,997,979     | 9,984,061       | 2.0×    |
| small  | 5,001,555     | 4,998,575       | 1.0×    |
| medium | 1,428,529     | 2,500,479       | 1.8×    |

## Question 1
**How much faster is matrix edge lookup?**

Answer:
Matrix lookup is about 1.8–2× faster on tiny and medium networks and about the same on small networks.
This shows the matrix can be faster for edge checks, but the difference is not huge.

## Question 2
**Why is list lookup slower? Trace through the code.**

Answer:
In an adjacency list, checking for an edge requires scanning through a node’s neighbors.
This takes time proportional to the node’s degree.
In a matrix, checking an edge is a direct array lookup, which is constant time O(1).

## Question 3
**In what applications would fast edge lookup matter?**

Answer:
Fast edge lookup matters in applications that repeatedly check if specific edges exist, such as network security checks, connection validation, or dense graph simulations.