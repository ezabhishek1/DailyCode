from itertools import accumulate

class Solution:
    # ============================================================================
    # APPROACH 3: SUFFIX-MAX ARRAY WITH ON-THE-FLY PREFIX-MAX (Pythonic Hybrid)
    # ============================================================================
    # Time Complexity: O(n) - Two passes (one for suffix_max building, one for calculation)
    # Space Complexity: O(n) - One suffix_max array of size n
    #
    # ALGORITHM OVERVIEW:
    # This is a clever hybrid approach that balances space-time trade-off:
    #   1. Precompute: Build suffix_max array using Python's functional accumulate()
    #   2. On-the-fly: Calculate prefix_max dynamically while iterating
    #   3. Calculate: Water trapped using both prefix_max and suffix_max[i+1]
    #
    # KEY INSIGHT:
    # Water at position i = min(prefix_max, suffix_max[i+1]) - arr[i]
    # Note: We use suffix_max[i+1] because we need max from i+1 onwards, not from i
    #
    # WHY THIS APPROACH:
    # - Trades computational elegance for slight space optimization
    # - Uses Python's functional programming paradigm (accumulate)
    # - Avoids building full prefix array - calculates on the fly
    # - Clean, concise, and "Pythonic" implementation
    # ============================================================================
    
    def maxWater(self, arr):
        from itertools import accumulate
        
        # ========================================================================
        # STEP 1: BUILD SUFFIX_MAX ARRAY USING FUNCTIONAL APPROACH
        # ========================================================================
        # This step precomputes the maximum height from each position to the end
        # Using Python's accumulate() with max function for elegance
        
        # Step 1a: Reverse the array for right-to-left processing
        # reversed(arr) gives us: [arr[-1], arr[-2], ..., arr[0]]
        # Example: arr = [3, 0, 1, 0, 4, 0, 2]
        #          reversed(arr) = [2, 0, 4, 0, 1, 0, 3]
        
        # Step 1b: Apply accumulate with max function
        # accumulate(reversed(arr), max) computes running maximum from right to left
        # This gives us: [2, 2, 4, 4, 4, 4, 4]
        # - Position 0: max(2) = 2
        # - Position 1: max(2, 0) = 2
        # - Position 2: max(2, 0, 4) = 4
        # - Position 3: max(2, 0, 4, 0) = 4
        # - etc.
        
        suffix_max = list(accumulate(reversed(arr), max))
        # Now suffix_max = [2, 2, 4, 4, 4, 4, 4] (right-to-left maximums)
        
        # Step 1c: Reverse back to get left-to-right indexing
        # After reversing: [4, 4, 4, 4, 4, 2, 2]
        # This matches what we want: suffix_max[i] = max height from position i to end
        suffix_max.reverse()
        
        # Example: For arr = [3, 0, 1, 0, 4, 0, 2]
        #          suffix_max = [4, 4, 4, 4, 4, 2, 2]  ✓ Correct!
        
        # ========================================================================
        # STEP 2: ITERATE THROUGH ARRAY AND CALCULATE TRAPPED WATER
        # ========================================================================
        # We calculate prefix_max on-the-fly during this single pass
        # This avoids needing a separate prefix array
        
        prefix_max = arr[0]  # Maximum height seen from current position leftward
        water = 0            # Accumulator for total trapped water
        
        # Loop through indices 1 to len(arr)-2 (skip first and last elements)
        # Why skip edges? First and last elements cannot trap water (no wall on one side)
        for i in range(1, len(arr) - 1):
            # At position i:
            # - prefix_max = maximum height from position 0 to i-1
            # - suffix_max[i+1] = maximum height from position i+1 to end
            # - arr[i] = current block height
            
            # Water level at position i is bounded by the smaller of the two maxima
            # Water trapped = min(left_max, right_max) - current_height
            water_level = min(prefix_max, suffix_max[i + 1])
            
            # Calculate water at this position
            # Use max(0, ...) to avoid negative values (though formula should prevent this)
            water += max(0, water_level - arr[i])
            
            # Update prefix_max for next iteration
            # Now include current element in the prefix maximum
            prefix_max = max(prefix_max, arr[i])
        
        # ========================================================================
        # EXAMPLE TRACE: [3, 0, 1, 0, 4, 0, 2]
        # ========================================================================
        # suffix_max = [4, 4, 4, 4, 4, 2, 2]
        #
        # i=1: prefix_max=3, suffix_max[2]=4, min(3,4)-0 = 3, water=3
        #      Update prefix_max = max(3,0) = 3
        # i=2: prefix_max=3, suffix_max[3]=4, min(3,4)-1 = 2, water=5
        #      Update prefix_max = max(3,1) = 3
        # i=3: prefix_max=3, suffix_max[4]=4, min(3,4)-0 = 3, water=8
        #      Update prefix_max = max(3,0) = 3
        # i=4: prefix_max=3, suffix_max[5]=2, min(3,2)-4 = -2 → max(0,-2)=0, water=8
        #      Update prefix_max = max(3,4) = 4
        # i=5: prefix_max=4, suffix_max[6]=2, min(4,2)-0 = 2, water=10
        #      Update prefix_max = max(4,0) = 4
        #
        # Total water = 10 ✓ CORRECT!
        
        return water


# ============================================================================
# COMPARISON OF THREE APPROACHES:
# ============================================================================
# Approach 1 (C++): Two-Pointer
#   - O(n) time, O(1) space
#   - Single pass, complex logic
#   - Best for performance
#
# Approach 2 (Python): Full Prefix-Suffix Arrays
#   - O(n) time, O(n) space
#   - Three passes, very clear logic
#   - Best for learning/interviews
#
# Approach 3 (Python): Hybrid with On-the-Fly Prefix
#   - O(n) time, O(n) space
#   - Two passes, elegant/Pythonic
#   - Best for demonstrating Python mastery
# ============================================================================
