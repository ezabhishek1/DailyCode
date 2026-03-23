class Solution:
    def longestCycle(self, V, edges):
        # Convert edges to adjacency list (since max 1 outgoing edge)
        adj = [-1] * V
        for u, v in edges:
            adj[u] = v
        
        visited = [False] * V
        max_cycle = -1

        for i in range(V):
            if visited[i]:
                continue

            curr = i
            step_map = {}   # node -> step
            step = 0

            while curr != -1:
                if visited[curr]:
                    break

                visited[curr] = True
                step_map[curr] = step
                step += 1

                next_node = adj[curr]

                # Cycle detected
                if next_node in step_map:
                    cycle_length = step - step_map[next_node]
                    max_cycle = max(max_cycle, cycle_length)
                    break

                curr = next_node

        return max_cycle