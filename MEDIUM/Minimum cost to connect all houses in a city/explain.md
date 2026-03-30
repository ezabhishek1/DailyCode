🏡💰 Minimum Cost to Connect All Houses: Kruskal's Algorithm with DSU
This problem requires connecting all houses (represented as 2D coordinates) with minimum cost, where the cost between two houses is the Manhattan Distance. The solution involves Kruskal's Algorithm along with Disjoint Set Union (DSU) for efficient cycle detection.



🔍 Intuition
We need to connect all houses (nodes) with the least total cost (sum of edges).

This is a classic Minimum Spanning Tree (MST) problem.

Kruskal's Algorithm is suitable because it processes edges in increasing order and uses DSU to avoid cycles.




🚀 Approach
Compute All Possible Edges:

For every pair of houses, calculate the Manhattan Distance (edge cost).

Store these edges in a min-heap (priority queue) to always pick the smallest cost edge first.

Kruskal's Algorithm with DSU:

Use a Disjoint Set Union (DSU) to detect cycles.

Process edges in increasing order:

If two nodes are in different sets, merge them and add the edge cost to the answer.

If they are in the same set, skip (to avoid cycles).

Termination:

The algorithm stops when all nodes are connected (forming an MST).






⏳ Time & Space Complexity
Time Complexity: O(N² log N) (due to sorting edges via priority queue).

Space Complexity: O(N²) (for storing edges).





