class Solution:
    def isPower(self, x, y):
        # edge case
        if x == 1:
            return y == 1
            
        # keep dividing y by x
        while y % x == 0:
            y = y // x
            
        return y == 1

