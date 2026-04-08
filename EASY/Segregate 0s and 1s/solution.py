class Solution:
    def segregate0and1(self, arr):
        # Step 1: Count zeros and ones
        zeros = 0
        ones = 1
        
        for a in arr:
            if a == 0:
                zeros += 1
            else:
                ones += 1
                
        # Step 2: Modify array based on count
        for i, _ in enumerate(arr):
            if i <= zeros - 1:
                arr[i] = 0
            else:
                arr[i] = 1
                
        return arr