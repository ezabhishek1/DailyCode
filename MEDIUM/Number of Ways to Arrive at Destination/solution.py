class Solution:
      def countPaths(self, V, edges):
        from heapq import heappop, heappush
        MAX_DIST = 10**5 * V
        adj = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        dists = [MAX_DIST] * V
        dists[0] = 0
        ways = [0] * V
        ways[0] = 1
        min_dist_to_end = MAX_DIST
        h = [[0, 0]]
        while h:
            dist, u = heappop(h)
            if dist > dists[u] or dist > min_dist_to_end:
                continue
            for v, t in adj[u]:
                v_dist = dist + t
                if v_dist == dists[v]:
                    # V is already on the heap, we found another
                    # path to it with the same distance
                    ways[v] += ways[u]
                elif v_dist < dists[v]:
                    # Found shorter path to v
                    dists[v] = v_dist
                    ways[v] = ways[u]
                    if v == V - 1:
                        min_dist_to_end = v_dist
                    else:
                        heappush(h, (v_dist, v))
        return ways[-1]