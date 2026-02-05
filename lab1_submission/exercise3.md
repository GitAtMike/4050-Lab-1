# Exercise 3 - Algorithm Performance

## Dijkstra Timing Results

| Network | List Dijkstra | Matrix Dijkstra | Slowdown |
| ------- | ------------- | --------------- | -------- |
| tiny    | 0.0000s       | 0.0002s         | N/A      |
| small   | 0.0020s       | 0.0176s         | 8.8×     |
| medium  | 0.0302s       | 2.4640s         | 81.6×    |

## Question 1
**Why is matrix-based Dijkstra slower despite O(1) edge lookup?**

Answer:
Even though matrix lookup is O(1), Dijkstra’s algorithm repeatedly iterates through it's neighbors.
In a matrix, checking neighbors requires scanning an entire row of V nodes each time, which takes longer.
Lists only scan actual neighbors, so they are faster.

## Question 2
**Where in the algorithm does the slowdown occur?**

Answer:
The slowdown happens during neighbor iteration as answered in the previous question.
The matrix must check every possible node connection, while the list only checks real edges.
This difference becomes huge as the graph grows in size.

## Question 3
**For what graph density would matrix be faster?**

Answer:
A matrix would be faster in very dense graphs where most nodes connect to most other nodes.
In that case, scanning a full row isn’t much extra work because many edges exist anyway.