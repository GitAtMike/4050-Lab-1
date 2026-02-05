# Exercise 5 — Real-World Decision Making

## Scenario 1 — Google Maps routing
**Choice:** Adjacency List
**Justification:** Each road intersection only connects to a few others (avg degree ~4), so the graph is very sparse.
                   An adjacency list makes more sense because it only stores real roads and won’t waste huge amounts of memory like a matrix would.

---

## Scenario 2 — Social network analysis
**Choice:** Adjacency List
**Justification:** Even though 200 friends sounds like a lot, it’s tiny compared to all possible connections between billions of users.
                   A matrix would be insanely large, so a list is the only realistic option since it stores only actual friendships.

---

## Scenario 3 — Circuit analysis
**Choice:** Adjacency List
**Justification:** Each component connects to only a few others, so most possible connections don’t exist.
                   A list works better here because it avoids storing a bunch of empty connections.

---

## Scenario 4 — Dense communication matrix
**Choice:** Adjacency Matrix
**Justification:** Since every server connects to every other server, the graph is dense.
                   In this case a matrix makes sense because most entries are actually used, and edge lookups are fast.
