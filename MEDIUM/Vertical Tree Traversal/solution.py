class Solution:
    def helper(self, root, level, mp):
        q = []
        q.append((0,root))
        
        while len(q) > 0:
            col, node = q.pop(0)
            
            if col not in mp:
                mp[col] = []
            mp[col].append(node.data)
            
            if node.left is not None:
                q.append((col - 1, node.left))
            if node.right is not None:
                q.append((col + 1, node.right))
                
    def verticalOrder(self, root): 
        mp = {}
        ans = []
        
        self.helper(root, 0, mp)
        
        keys = list(mp.keys())
        keys.sort()
        
        for k in keys:
            ans.append(mp[k])
        
        return ans