🏡💰 Minimum Cost to Connect All Houses: Kruskal's Algorithm with DSU
This problem requires connecting all houses (represented as 2D coordinates) with minimum cost, where the cost between two houses is the Manhattan Distance. The solution involves Kruskal's Algorithm along with Disjoint Set Union (DSU) for efficient cycle detection.



🔍 Intuition
We need to connect all houses (nodes) with the least total cost (sum of edges).

This is a classic Minimum Spanning Tree (MST) problem.

Kruskal's Algorithm is suitable because it processes edges in increasing order and uses DSU to avoid cycles.


