class Solution:
    def getSize(self, root):
        # code here
        if root==None:
            return 0
            
        return 1+self.getSize(root.left)+self.getSize(root.right)