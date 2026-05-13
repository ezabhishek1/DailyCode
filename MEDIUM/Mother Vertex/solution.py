class Solution:
    def findMotherVertex(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges: adj[u].append(v)

        def dfs(u, vis):
            vis[u] = 1
            for v in adj[u]:
                if not vis[v]: dfs(v, vis)

        # find candidate
        vis, cand = [0]*V, -1
        for i in range(V):
            if not vis[i]:
                dfs(i, vis)
                cand = i

        # verify candidate
        vis = [0]*V
        dfs(cand, vis)
        if sum(vis) < V: return -1

        # check smallest valid
        ans = cand
        for i in range(V):
            vis = [0]*V
            dfs(i, vis)
            if sum(vis) == V: ans = min(ans, i)
        return ans