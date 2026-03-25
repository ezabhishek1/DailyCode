## C++ Solution using BFS (Leaf Trimming / Topological Approach) --> See the Python solution for a recursive approach 




# Instead of calculating height from every node (which is slow), we remove leaf nodes layer by layer.

- This approach is known as Topological / BFS trimming.

## Intuition:

### Think of the tree like an onion.
- Remove the outer layer (leaf nodes)
- Keep removing layer by layer
- The last remaining nodes are the center

These center nodes give the Minimum Height Trees.


## cpp version 

💡 Intuition (Core Idea)
A Minimum Height Tree is formed when the root is as close as possible to all nodes.

👉 The farthest nodes in a tree are always the leaves.
👉 If we remove leaves layer by layer, we move toward the center of the tree.

Think of it like peeling an onion 🧅:

Outer layer = leaves
Keep removing them
The last 1 or 2 nodes left = centroids
👉 These centroids give minimum height.