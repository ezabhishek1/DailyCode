class Solution:    
    def findUnion(self, a, b):
        c=set()
        for x in a:
            c.add(x)
        for x in b:
            c.add(x)
                
        return c