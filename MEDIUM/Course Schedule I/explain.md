Algorithm: Kahn's Algorithm (Topological Sort)

Real-World Example: A university student must complete Intro Programming before Data Structures; if classes require each other cyclically, graduation is impossible.

Complexities: Time: $O(V + E)$, Space: $O(V + E)$


# We treat courses as a directed graph.

###  If there is a cycle, we cannot complete all courses.

### Use Topological Sort (BFS / Kahn’s Algorithm):

-  Build adjacency list
- Calculate indegree of each node
- Push all nodes with indegree 0 into queue
- Process queue:
- - remove node
- - reduce indegree of neighbors
- - if indegree becomes 0 → push to queue
- If all nodes are processed → return true
- - else → cycle exists → return false