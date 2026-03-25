# Instead of calculating height from every node (which is slow), we remove leaf nodes layer by layer.

- This approach is known as Topological / BFS trimming.

## Intuition:

### Think of the tree like an onion.
- Remove the outer layer (leaf nodes)
- Keep removing layer by layer
- The last remaining nodes are the center

These center nodes give the Minimum Height Trees.