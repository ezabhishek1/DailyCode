# Approach

I used recursion to traverse the whole tree.

## Step-by-step:

### If the current node is NULL, I return 0 because there is no node to count.

### Otherwise, I recursively calculate:

- size of the left subtree

- size of the right subtree

### Then I add both values and include the current node by adding 1.

### The final returned value becomes the total number of nodes in that subtree.

## This process continues until all nodes are visited exactly once.