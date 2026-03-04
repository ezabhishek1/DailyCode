class Solution {
  public:
    // Approach 1: Sliding Window with Index
    int maxSubarrayXOR(vector<int>& arr, int k) {
        int n = arr.size();
        
        // Calculate XOR of first window
        int currentXor = 0;
        for(int i = 0; i < k; i++) {
            currentXor ^= arr[i];
        }
        
        int maxXor = currentXor;
        
        // Slide the window and update XOR
        for(int i = k; i < n; i++) {
            // Remove the leftmost element of previous window
            currentXor ^= arr[i - k];
            // Add the new rightmost element
            currentXor ^= arr[i];
            maxXor = max(maxXor, currentXor);
        }
        
        return maxXor;
    }
    
    // Approach 2: Two Pointer Logic
    int maxSubarrayXORTwoPointer(vector<int>& arr, int k) {
        int n = arr.size();
        int maxXor = INT_MIN;
        int currentXor = arr[0];
        
        int l = 0, r = 1;
        while(l <= n - k) {
            if(r - l + 1 > k) {
                maxXor = max(maxXor, currentXor);
                currentXor ^= arr[l];
                l++;
            }
            currentXor ^= arr[r];
            r++;
        }
        
        if(maxXor == INT_MIN) {
            return currentXor;
        }
        return maxXor;
    }
};