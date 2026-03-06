class Solution {
  public:
    /**
     * Helper function to check if current window contains all required characters
     * @param ms - Current window character frequency map
     * @param mp - Pattern character frequency map (requirements)
     * @return true if window contains all required characters with sufficient count
     */
    bool check(unordered_map<int,int>&ms, unordered_map<int,int>&mp){
        // If window has fewer unique characters than pattern needs, invalid window
        if(ms.size() < mp.size())
            return false;
        
        // Check each required character in pattern
        for(auto it : mp){
            // If this character appears more times in pattern than in window, invalid
            if(it.second > ms[it.first])
                return false;
        }
        
        // All required characters have sufficient frequency in window
        return true;
    }
    
    /**
     * Find the minimum window substring that contains all characters in pattern p
     * Uses sliding window approach with two pointers
     * 
     * Time Complexity: O(n * m) where n = len(s), m = unique chars
     * Space Complexity: O(1) - at most 26 lowercase letters
     */
    string minWindow(string &s, string &p) {
        // Create frequency map for pattern
        // Maps each character to how many times we need it
        // Example: p="ABC" -> mp = {A:1, B:1, C:1}
        unordered_map<int,int> mp;
        for(auto it : p)
            mp[it]++;  // Count occurrences of each character in pattern
        
        // Initialize result and tracking variables
        string ans = "";           // Stores the smallest window found
        int i = 0;                 // Left pointer of sliding window
        int j = 0;                 // Right pointer of sliding window
        
        // Frequency map for current window characters
        // Updated as we expand and shrink the window
        unordered_map<int,int> ms;
        
        // SLIDING WINDOW LOOP
        // Continue while both pointers are within bounds
        while(i < s.size() && j < s.size()){
            // PHASE 1: EXPAND WINDOW
            // Add character at position j to current window
            ms[s[j]]++;  // Increment count of s[j] in current window
            
            // PHASE 2: SHRINK WINDOW
            // Keep shrinking window from left while it contains all required chars
            while(check(ms, mp) && i < s.size()){
                // Current window is valid (has all characters)
                // Check if this window is smaller than our previous best
                if(ans == "" || ans.size() > j - i + 1)
                    ans = s.substr(i, j - i + 1);  // Store this window
                
                // Try to shrink window by removing leftmost character
                ms[s[i]]--;  // Decrease frequency of leftmost character
                
                // If count becomes 0, remove from map to keep it clean
                if(ms[s[i]] == 0)
                    ms.erase(s[i]);
                
                // Move left pointer forward (shrink window)
                i++;
            }
            
            // Move right pointer forward (expand window)
            j++;
        }
        
        // Return the smallest window found, or empty string if no valid window exists
        return ans;
    }
};