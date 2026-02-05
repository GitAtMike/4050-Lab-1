# Exercise 1 -  Memory Scaling Analysis

## Memory Usage Results

| Network | Nodes         | List Memory | Matrix Memory | Ratio |
| ------- | ------------- | ----------- | ------------- | ----- |
| tiny    | 100           | 0.1 MB      | 0.1 MB        | 1.3×  |
| small   | 961           | 0.7 MB      | 7.4 MB        | 10.6× |
| medium  | 10,000        | 9.3 MB      | 766.7 MB      | 82.9× |
| large   | N/A (not run) | N/A         | N/A           | N/A   |

Didn't run large as the matrix becomes impractical at this scale and avoid excessive use of memory

## Question 1:
**What is the relationship between node count and matrix memory?**

Answer:
Matrix memory grows with nodes² because it stores a value for every possible pair of nodes.
So when nodes increase, memory shoots up fast.
My results showed matrix memory jumping from 7.4 MB at ~1k nodes to 766.7 MB at 10k nodes, while the list grew much slower.

## Question 2:
**At what size does the matrix become impractical?**

Answer:
It starts becoming impractical around 10,000 nodes since it already uses ~767 MB.
Around 100,000 nodes it’s basically not usable because it needs too much memory.

## Question 3:
**Predict the memory for 200,000 nodes. Would it fit in 32GB?**

Answer:
A 200k × 200k matrix has 40 billion entries. At ~8 bytes each, that’s about 320 GB. So it would not fit in 32GB.