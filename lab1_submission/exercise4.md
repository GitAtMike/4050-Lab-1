# Exercise 4 — The Breaking Point (Demonstration)

## Memory usage before loading

- RAM used before starting: 14.5/31.9 GB

## During matrix allocation / loading

- Peak RAM used: No big increase, due to OS stopping it

- How long it ran before slowing/freezing/stopping: Stopped almost immediately once ran

## What happened when memory was exhausted

- Result: Program raised a MemoryError and stopped

- Terminal error message:
    MemoryError: Matrix would require ~74.3GB RAM! Use adjacency list for graphs with >57926 nodes.