class Solution:
    # ============================================================================
    # APPROACH 2: PREFIX-SUFFIX MAXIMUM ARRAYS (Three Pass, Very Clear Logic)
    # ============================================================================
    # Time Complexity: O(n) - Three linear passes through array (3*n = O(n))
    # Space Complexity: O(n) - Two auxiliary arrays of size n each
    #
    # ALGORITHM OVERVIEW:
    # This approach prioritizes CLARITY over space efficiency.
    # It separates the solution into three distinct, easy-to-understand phases:
    #   1. Precompute: Find max height from start to each position (left array)
    #   2. Precompute: Find max height from each position to end (right array)
    #   3. Calculate: For each position, water = min(left_max, right_max) - height
    #
    # KEY INSIGHT:
    # Water at position i = min(left[i], right[i]) - arr[i]
    # where left[i] = maximum height from position 0 to i
    #       right[i] = maximum height from position i to n-1
    #
    # WHY THIS WORKS:
    # The water level at any position is bounded by the MINIMUM of the tallest
    # barriers on both sides. We precompute these barriers explicitly.
    # ============================================================================
    
    def maxWater(self, arr):
        n = len(arr)
        
        # ========================================================================
        # PHASE 1: BUILD LEFT ARRAY (Maximum from start to each position)
        # ========================================================================
        # For each position i, left[i] stores the maximum height from index 0 to i
        # This represents the tallest barrier/wall on the LEFT side of position i
        
        m1 = 0                  # Variable to track the current maximum from left
        left = [0] * n          # Array to store max height up to each position
        
        for i in range(n):
            # Update m1 to be the maximum between current max and current element
            m1 = max(m1, arr[i])
            # Store the maximum height seen so far at position i in the left array
            # left[i] = max(arr[0], arr[1], ..., arr[i])
            left[i] = m1
        
        # Example: If arr = [3, 0, 1, 0, 4, 0, 2]
        #          Then left = [3, 3, 3, 3, 4, 4, 4]
        #          (max from start to each position)
        
        # ========================================================================
        # PHASE 2: BUILD RIGHT ARRAY (Maximum from each position to end)
        # ========================================================================
        # For each position i, right[i] stores the maximum height from index i to n-1
        # This represents the tallest barrier/wall on the RIGHT side of position i
        
        m2 = 0                  # Variable to track the current maximum from right
        right = [0] * n         # Array to store max height from each position to end
        
        for i in range(n):
            # Scan from right to left: n-1, n-2, ..., 0
            # arr[n-i-1] gives us the element at position n-1-i
            m2 = max(m2, arr[n-i-1])
            # Store the maximum height seen from position (n-i-1) to end
            # right[n-i-1] = max(arr[n-i-1], arr[n-i], ..., arr[n-1])
            right[n-i-1] = m2
        
        # Example: If arr = [3, 0, 1, 0, 4, 0, 2]
        #          Then right = [4, 4, 4, 4, 4, 2, 2]
        #          (max from each position to end)
        
        # ========================================================================
        # PHASE 3: CALCULATE TRAPPED WATER AT EACH POSITION
        # ========================================================================
        # Now that we have precomputed both left and right maxima,
        # we can calculate trapped water using the simple formula:
        # water_at_position_i = min(left[i], right[i]) - arr[i]
        
        water = 0               # Accumulator for total water trapped
        
        for i in range(n):
            # For each position, calculate how much water can be trapped
            # The water level is determined by the SMALLER of the two max heights
            # (the bottleneck principle)
            # Then subtract the block height at this position
            
            water_level = min(left[i], right[i])    # Water surface level at position i
            block_height = arr[i]                    # Height of block at position i
            water += water_level - block_height      # Water trapped = level - block
        
        # Example: For arr = [3, 0, 1, 0, 4, 0, 2]
        # Position 0: min(3, 4) - 3 = 0  (no trapped water)
        # Position 1: min(3, 4) - 0 = 3  (3 units trapped)
        # Position 2: min(3, 4) - 1 = 2  (2 units trapped)
        # Position 3: min(3, 4) - 0 = 3  (3 units trapped)
        # Position 4: min(4, 4) - 4 = 0  (no trapped water)
        # Position 5: min(4, 2) - 0 = 2  (2 units trapped)
        # Position 6: min(4, 2) - 2 = 0  (no trapped water)
        # Total = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 ✓
        
        return water
        