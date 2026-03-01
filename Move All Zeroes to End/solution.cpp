class Solution {
  public:
    // Approach 1: Swap-Based Two-Pointer (Single Pass)
    // Time Complexity: O(n) - Single pass through array
    // Space Complexity: O(1) - In-place modification, only two pointers
    // 
    // Algorithm: Uses two pointers moving from left to right
    // - Pointer 'l': Tracks the position where next non-zero element should go
    // - Pointer 'i': Current element being scanned
    // When a non-zero element is found, swap it with position at 'l'
    void pushZerosToEnd(vector<int>& arr) {
        int l = 0, sizeOfArr = arr.size();
        
        // Single pass: scan entire array
        for (int i = 0; i < sizeOfArr; i++) {
            // If current element is non-zero
            if (arr[i]) {
                // Swap with position at 'l' and move 'l' forward
                // This ensures all non-zeros are at front, zeros fall to back
                swap(arr[i], arr[l++]);
            }
        }
        // After loop: all non-zero elements are at front, zeros naturally at end
    }
};