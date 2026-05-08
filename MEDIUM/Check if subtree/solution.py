# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    
    # Function to check if two trees are identical
    def isIdentical(self, a, b):
        
        # If both are None
        if not a and not b:
            return True
        
        # If one is None and other is not
        if not a or not b:
            return False
        
        # Check current node and subtrees
        return (a.data == b.data and
                self.isIdentical(a.left, b.left) and
                self.isIdentical(a.right, b.right))
    
    def isSubTree(self, root1, root2):
        
        # If subtree is empty
        if not root2:
            return True
        
        # If main tree is empty
        if not root1:
            return False
        
        # Check if trees are identical from current node
        if self.isIdentical(root1, root2):
            return True
        
        # Otherwise search in left and right subtree
        return (self.isSubTree(root1.left, root2) or
                self.isSubTree(root1.right, root2))