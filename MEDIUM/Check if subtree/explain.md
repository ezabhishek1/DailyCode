# Approach
I used recursion for this problem.

First, I created a helper function called isSame().

This function checks whether two trees are identical.

## Rules:

If both nodes are NULL, return true

If one is NULL and the other is not, return false

If values are different, return false

Otherwise, recursively compare left and right subtrees

After that, I traversed the main tree root1.

At every node:

I checked whether the subtree starting from this node is identical to root2

If yes, return true

Otherwise, continue searching in left and right subtrees

If no matching subtree is found anywhere, return false.