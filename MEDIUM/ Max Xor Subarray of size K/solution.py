class Solution:
    # Approach 1: Sliding Window with Index
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        
        # Calculate XOR of first window
        current_xor = 0
        for i in range(k):
            current_xor ^= arr[i]
        
        max_xor = current_xor
        
        # Slide the window and update XOR
        for i in range(k, n):
            # Remove the leftmost element of previous window
            current_xor ^= arr[i - k]
            # Add the new rightmost element
            current_xor ^= arr[i]
            max_xor = max(max_xor, current_xor)
        
        return max_xor
    
    # Approach 2: Two Pointer Logic
    def maxSubarrayXORTwoPointer(self, arr, k):
        n = len(arr)
        max_xor = float('-inf')
        current_xor = arr[0]
        
        l = 0
        r = 1
        while l <= n - k:
            if r - l + 1 > k:
                max_xor = max(max_xor, current_xor)
                current_xor ^= arr[l]
                l += 1
            current_xor ^= arr[r]
            r += 1
        
        if max_xor == float('-inf'):
            return current_xor
        return max_xor