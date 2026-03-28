🧠 Intuition (very easy)
Think of graph like a network.

👉 An articulation point is a node which, if removed, breaks the graph into more pieces.


🔥 Key idea (Tarjan’s Algorithm)
We use DFS and track 2 things:

1. tin[node] → time when node is first visited
2. low[node] → lowest reachable time from that node