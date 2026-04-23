class Solution:
    def canSplit(self, arr):
        total = sum(arr)
        
        # if total sum is odd, split cannot equally
        if total % 2 != 0:
            return False
            
        target = total // 2
        prefix_sum = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            # Check if we found a valid split point
            if prefix_sum == target:
                return True
                
        return False