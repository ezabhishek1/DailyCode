class Solution:
    def condition(self, a, b):
        return  a*b < 0 and abs(a) != abs(b)
    
    def equal(self, a, b):
        return a * b < 0 and abs(a) == abs(b)
        
    def reducePairs(self, arr):
        # code here
        res = []
        
        for curr in arr:
            # 0 is neither positive nor negative
            if curr == 0:
                continue
            
            # opposite sign and diff value -> take the abs max(preserve sign)
            while res and self.condition(res[-1], curr):
                prev = res.pop()
                curr = curr if (abs(curr) > abs(prev)) else prev
            
            # opposite sign and equal absolute value -> remove both
            if res and self.equal(res[-1], curr):
                res.pop()
            else:
                res.append(curr)
            
        return res