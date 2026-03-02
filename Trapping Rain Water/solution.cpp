class Solution {
  public:
    // Approach 1: Two-Pointer with Max Tracking
    // Time Complexity: O(n) - Single pass through array
    // Space Complexity: O(1) - Only constant extra space for pointers and max variables
    //
    // Algorithm: Use two pointers from both ends, tracking maximum heights seen so far
    // Key Insight: Water at position i = min(max_left, max_right) - arr[i]
    // We move from the side with smaller height since it's the bottleneck
    
    int maxWater(vector<int> &arr) {
        if (arr.empty()) return 0;

        int left = 0, right = arr.size() - 1;
        int left_max = 0, right_max = 0;  // Track max height from each side
        int water_trapped = 0;

        // Two pointers move towards each other
        while (left <= right) {
            // If left side is shorter/equal, process from left
            if (arr[left] <= arr[right]) {
                // Update left_max if current height is taller
                if (arr[left] >= left_max) {
                    left_max = arr[left]; 
                } else {
                    // Water can be trapped: difference between max and current height
                    water_trapped += left_max - arr[left];  
                }
                left++;
            } 
            // If right side is shorter, process from right
            else {
                // Update right_max if current height is taller
                if (arr[right] >= right_max) {
                    right_max = arr[right]; 
                } else {
                    // Water can be trapped: difference between max and current height
                    water_trapped += right_max - arr[right];  
                }
                right--;
            }
        }

        return water_trapped;
    }
};