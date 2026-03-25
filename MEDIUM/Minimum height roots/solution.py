class Solution:
    def minHeightRoot(self, V, edges):
        adjList = defaultdict(list)
        indegree = [0] * V
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
            indegree[u] += 1
            indegree[v] += 1
            
        queue = deque([i for i in range(V) if indegree[i] == 1])
        nodeCount = V
        
        while queue and nodeCount > 2:
            size = len(queue)
            nodeCount -= size
            
            for _ in range(size):
                src = queue.popleft()
                
                for nbr in adjList[src]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 1:
                        queue.append(nbr)
        return list(queue)
