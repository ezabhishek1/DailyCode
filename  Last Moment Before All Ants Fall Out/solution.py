class Solution:
    def getLastMoment(self, n, left, right):
        max_time = 0
        
        # Ants moving to the left
        for pos in left:
            max_time = max(max_time, pos)
        
        # Ants moving to the right
        for pos in right:
            max_time = max(max_time, n - pos)
        
        return max_time

