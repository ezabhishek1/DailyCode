from collections import defaultdict

class Solution:
    # ============================================================================
    # APPROACH: Sliding Window with defaultdict (Two Pointers)
    # ============================================================================
    # Time Complexity: O(n) - Each element visited at most twice (i and j pointers)
    # Space Complexity: O(1) - Dictionary stores at most 2 distinct elements
    #
    # ALGORITHM OVERVIEW:
    # Use two pointers (sliding window) with a dictionary for element tracking.
    # Expand window by moving right pointer j, shrink by moving left pointer i.
    # Maintain constraint: at most 2 distinct elements in current window.
    # Track the maximum valid window size.
    #
    # WHY THIS WORKS:
    # - defaultdict(int) automatically initializes missing keys to 0
    # - len(dic) gives count of distinct elements
    # - When distinct count exceeds 2, shrink window from left
    # - Amortized O(n) even with nested loops because pointers move forward only
    # ============================================================================
    
    def totalElements(self, arr):
        dic = defaultdict(int)              # Dictionary for {element: frequency}
        i = 0                               # Left pointer of sliding window
        j = 0                               # Right pointer of sliding window
        maxi = 0                            # Track maximum valid window length
        
        # ========================================================================
        # TWO-POINTER SLIDING WINDOW
        # ========================================================================
        while j < len(arr) and i < len(arr):
            # Step 1: Expand window by adding element at position j
            dic[arr[j]] += 1
            
            # Step 2: Check if constraint is satisfied (at most 2 distinct)
            if len(dic) <= 2:
                # Window is valid: all elements with <= 2 distinct values
                # Update maximum length: window_size = j - i + 1
                # Example: if i=1, j=4, window_size = 4-1+1 = 4
                maxi = max(maxi, j - i + 1)
                # Move right pointer to expand window further
                j += 1
            
            else:
                # Window is invalid: more than 2 distinct elements
                # Need to shrink from left side
                
                # Decrement frequency of left element
                dic[arr[i]] -= 1
                
                # If frequency becomes 0, remove from dictionary
                # This reduces distinct count, making room for expansion
                if dic[arr[i]] == 0:
                    del dic[arr[i]]
                
                # Move both pointers forward
                # This shrinks window from left and attempts expansion from right
                i += 1
                j += 1
        
        # Step 3: Final check after while loop exits
        # Ensure we capture the maximum length with remaining valid window
        maxi = max(maxi, j - i)
        
        return maxi