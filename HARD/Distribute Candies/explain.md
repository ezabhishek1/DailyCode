Approach:
---------
We solve this problem using Postorder DFS traversal.

Key Idea:
Each node should have exactly 1 candy.
If a node has extra candies, it will pass them to its parent.
If a node has fewer candies, it will receive from its parent.

For each node, we calculate:
    extra = node->data - 1

- If extra > 0 → node gives candies to parent
- If extra < 0 → node needs candies from parent