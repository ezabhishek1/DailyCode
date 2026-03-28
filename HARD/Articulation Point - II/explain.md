🧠 Intuition (very easy)
Think of graph like a network.

👉 An articulation point is a node which, if removed, breaks the graph into more pieces.


🔥 Key idea (Tarjan’s Algorithm)
We use DFS and track 2 things:

1. tin[node] → time when node is first visited
2. low[node] → lowest reachable time from that node




⚡ Important conditions
Case 1: Root node
If root has more than 1 child → it’s articulation point
Case 2: Non-root node
If for a child v:

👉 low[v] >= tin[u]
→ then u is articulation point



A R
12 hours agoMar 28, 2026 15:49 (GMT +5:30)

🧠 Intuition (very easy)
Think of graph like a network.

👉 An articulation point is a node which, if removed, breaks the graph into more pieces.

🔥 Key idea (Tarjan’s Algorithm)
We use DFS and track 2 things:

1. tin[node] → time when node is first visited
2. low[node] → lowest reachable time from that node
⚡ Important conditions
Case 1: Root node
If root has more than 1 child → it’s articulation point
Case 2: Non-root node
If for a child v:

👉 low[v] >= tin[u]
→ then u is articulation point

🧩 Step-by-step flow
Build adjacency list
Run DFS for all components (graph may be disconnected)
Track:
visited[]
tin[]
low[]
Apply above conditions

### reffer to cpp code version


⏱ Complexity
Time: O(V + E)
Space: O(V + E)
