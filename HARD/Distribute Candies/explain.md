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


DFS Logic:
----------
1. Traverse left subtree → get left extra
2. Traverse right subtree → get right extra
3. Total moves required at this node:
       moves += abs(left) + abs(right)

   (because each candy movement across an edge counts as 1 move)

4. Return total extra candies to parent:
       return node->data + left + right - 1