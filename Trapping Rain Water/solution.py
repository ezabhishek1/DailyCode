class Solution:
    # Approach 2: Prefix-Suffix Maximum Arrays
    # Time Complexity: O(n) - Three linear passes through array (3*n = O(n))
    # Space Complexity: O(n) - Two auxiliary arrays of size n
    #
    # Algorithm: Precompute max heights on both sides, then calculate trapped water
    # Key Insight: Water at position i = min(left[i], right[i]) - arr[i]
    # This approach prioritizes clarity over space efficiency
    
    def maxWater(self, arr):
        n = len(arr)
        
        # Step 1: Build left array - max height from start to each position
        m1 = 0  # Current max from left
        left = [0] * n
        for i in range(n):
            m1 = max(m1, arr[i])  # Update max as we scan left to right
            left[i] = m1  # Store max up to position i
        
        # Step 2: Build right array - max height from each position to end
        m2 = 0  # Current max from right
        right = [0] * n
        for i in range(n):
            m2 = max(m2, arr[n-i-1])  # Update max scanning right to left
            right[n-i-1] = m2  # Store max from position i to end
        
        # Step 3: Calculate total trapped water
        # Water at each position = min of max heights on both sides - current height
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - arr[i]
        
        return water
        