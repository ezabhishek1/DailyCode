# hint 

Same as Dijkstra's Algorithm:

Just think of how to consider for all paths.
Paths will be considered for each node and summates if d+len==dist[neighbour], i.e., path[neighbour]+=path[node]
d+len<dist[neighbour], then path[neighbour]=path[node].

At the end return path[V-1]