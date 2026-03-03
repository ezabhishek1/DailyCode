class Solution {
  public:
    // ============================================================================
    // APPROACH 1: TWO-POINTER WITH MAX TRACKING (Single Pass)
    // ============================================================================
    // Time Complexity: O(n) - Single pass through array with two converging pointers
    // Space Complexity: O(1) - Only constant extra space (4 integer variables)
    //
    // ALGORITHM OVERVIEW:
    // Use two pointers moving towards each other from both ends of the array.
    // Maintain maximum heights seen so far from each direction.
    // At each position, the water level is determined by the smaller of the two max heights.
    //
    // KEY INSIGHT:
    // Water at position i = min(max_left, max_right) - arr[i]
    // We "move from the side with smaller height" because it acts as the bottleneck.
    // If arr[left] <= arr[right], we know for sure that the water level at 'left'
    // is bound by left_max (regardless of what's on the right).
    // ============================================================================
    
    int maxWater(vector<int> &arr) {
        // Edge case: empty array
        if (arr.empty()) return 0;

        // Step 1: Initialize pointers and variables
        int left = 0;                    // Pointer starting from left end
        int right = arr.size() - 1;      // Pointer starting from right end
        int left_max = 0;                // Maximum height seen from left side so far
        int right_max = 0;               // Maximum height seen from right side so far
        int water_trapped = 0;           // Accumulator for total water trapped

        // Step 2: Two pointers converge towards each other
        while (left <= right) {
            // Step 2a: Compare heights at both pointers
            if (arr[left] <= arr[right]) {
                // LEFT SIDE IS SHORTER OR EQUAL:
                // Process from the left side because left acts as bottleneck
                
                if (arr[left] >= left_max) {
                    // Current height is taller than any height we've seen from left
                    // This becomes the new boundary, no water can be trapped here
                    left_max = arr[left];
                } else {
                    // Current height is shorter than left_max
                    // Water can be trapped: the difference between max and current
                    // Formula: water_level = min(left_max, right_max) - arr[left]
                    // Since arr[left] <= arr[right], we know right side is taller,
                    // so water_level = left_max - arr[left]
                    water_trapped += left_max - arr[left];
                }
                // Move left pointer forward to process next element
                left++;
            } 
            else {
                // RIGHT SIDE IS SHORTER:
                // Process from the right side because right acts as bottleneck
                
                if (arr[right] >= right_max) {
                    // Current height is taller than any height we've seen from right
                    // This becomes the new boundary, no water can be trapped here
                    right_max = arr[right];
                } else {
                    // Current height is shorter than right_max
                    // Water can be trapped: the difference between max and current
                    // Formula: water_level = min(left_max, right_max) - arr[right]
                    // Since arr[left] > arr[right], we know left side is taller,
                    // so water_level = right_max - arr[right]
                    water_trapped += right_max - arr[right];
                }
                // Move right pointer backward to process next element
                right--;
            }
        }

        // Step 3: Return the total amount of water trapped
        return water_trapped;
    }
};