# Largest BST in Binary Tree

We need to find the size of the biggest subtree that is a valid BST.

 ## Main idea

-- Instead of checking every subtree again and again, we use postorder traversal.

#### Why postorder?

Because for any node, we must first know about its left subtree and right subtree before deciding whether the current subtree is a BST or not.

#### What we store for each subtree
  For every node, we return:

isBST → whether this subtree is a BST

min → smallest value in this subtree

max → largest value in this subtree

size → size of this subtree if it is a BST

Base case
For null node:

it is a BST

size = 0

min = +infinity

max = -infinity

This helps while checking leaf nodes easily.

### How to check BST at current node
For a node to form a BST:

left subtree must be BST

right subtree must be BST

current node value must be:

greater than left.max

smaller than right.min

If all these are true, then current subtree is also a BST.

Then:

size = left.size + right.size + 1

update the answer with the maximum size found so far

If not, mark it as invalid BST.

Why this works
Each node is processed only once, and we already know the result of its children from recursion. So we avoid repeated work.

Example
For tree:

[6, 7, 3, N, 2, 2, 4]

The largest BST subtree has size 3.



Time and Space Complexity
Time Complexity: O(N)
because every node is visited once

Space Complexity: O(H)
where H is the height of the tree because of recursion stack

Simple conclusion
The trick is to solve the problem from bottom to top.
For each node, first check left and right subtrees, then decide whether the whole subtree is BST or not.