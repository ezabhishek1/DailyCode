### The painful part of solving this in Python is that (a) it appears that the problem is just too large for a nice recursive solution and (b) that it is a huge headache trying to get why a recursive Python program fails here.  There's a tiny limit on how much stdout and stderr output the website will display.  It makes debugging feel like trying to play tennis on a pickleball court!


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
