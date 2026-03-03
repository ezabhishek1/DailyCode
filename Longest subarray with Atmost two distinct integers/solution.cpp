class Solution {
  public:
    // ============================================================================
    // APPROACH: Sliding Window with Hash Map (Two Pointers)
    // ============================================================================
    // Time Complexity: O(n) - Each element visited at most twice (j and i pointers)
    // Space Complexity: O(1) - Hash map stores at most 2 distinct elements
    //
    // ALGORITHM OVERVIEW:
    // Use two pointers (sliding window) with a map to track element frequencies.
    // Expand window by moving right pointer, shrink by moving left pointer.
    // Maintain constraint: at most 2 distinct elements in current window.
    // Track the maximum window size that satisfies this constraint.
    //
    // KEY INSIGHT:
    // - Expand right: Add new element to window
    // - If distinct count > 2: Shrink from left until constraint is satisfied
    // - Never need to backtrack left pointer (monotonic movement)
    // - Maximum valid window is guaranteed to be found
    // ============================================================================
    
    int totalElements(vector<int> &arr) {
        int n = arr.size();
        int i = 0;                          // Left pointer of sliding window
        int maxi = 0;                       // Track maximum window length
        map <int, int> mpp;                 // Map to store {element: frequency}
        
        // ========================================================================
        // SLIDING WINDOW: Right pointer j expands the window
        // ========================================================================
        for (int j = 0; j < n; j++){
            // Step 1: Add current element to the map
            // This expands our window to include arr[j]
            mpp[arr[j]]++;
            
            // Step 2: Check if window violates constraint (more than 2 distinct)
            // While we have more than 2 distinct elements, shrink from left
            while (mpp.size() > 2){
                // Decrement the frequency of left element
                mpp[arr[i]]--;
                
                // If frequency becomes 0, remove element from map
                // This reduces distinct count by 1
                if (mpp[arr[i]] == 0)
                    mpp.erase(arr[i]);
                
                // Move left pointer forward to shrink window
                i++;
            }
            
            // Step 3: Current window [i, j] is valid (has <= 2 distinct elements)
            // Update maximum length: window_size = j - i + 1
            // Example: if i=2, j=5, window_size = 5-2+1 = 4
            maxi = max(maxi, j - i + 1);
        }
        
        return maxi;
    }
};