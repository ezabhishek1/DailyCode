Approach (Simple & Intuitive):

First, traverse the tree using BFS and store the parent of every node in a map.
This helps in moving upward in the tree.

While creating the parent map, also locate the target node.

Start a BFS from the target node to simulate the burning process.
From each node, fire spreads to:

Left child

Right child

Parent

Maintain a visited map to avoid revisiting nodes.

Each level of BFS represents 1 second.
Count the number of levels until all nodes are burned.

⏱ Complexity:

Time Complexity: O(n)
Space Complexity: O(n)
