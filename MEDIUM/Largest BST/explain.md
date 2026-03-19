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