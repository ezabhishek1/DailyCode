## Python solution using `topological sort`:---

class Solution:
      def minHeightRoot(self, V, edges):
        adj = [[] for _ in range(V)]
        indeg = [0] * V
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        q = deque([u for u in range(V) if indeg[u] == 1])
        remaining_count = V
        while remaining_count > 2:
            remaining_count -= len(q)
            for _ in range(len(q)):
                u = q.popleft()
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 1:
                        q.append(v)
        return list(q)
