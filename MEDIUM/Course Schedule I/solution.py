class Solution:
    def canFinish(self, n, prerequisites):
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        for x, y in prerequisites:
            adj[y].append(x)
            indegree[x] += 1
            
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        count = 0
        front = 0
        
        while front < len(queue):
            node = queue[front]
            front += 1
            count += 1
            
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] ==0:
                    queue.append(nei)
                    
        return count == n