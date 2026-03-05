class Solution {
  public:
    int longestKSubstr(string &s, int k) {
        // HashMap to store frequency of characters in current window
        unordered_map<char,int> mp;
        int maxAns = -1;  // Initialize to -1 (no valid substring found yet)
        int j = 0;        // Left pointer of sliding window
        
        // Right pointer traversal
        for(int i = 0; i < s.length(); i++){
            // Add current character to window
            mp[s[i]]++;
            
            // Update answer when we have exactly k distinct characters
            if(mp.size() == k){
                int len = i - j + 1;  // Current window length
                maxAns = max(maxAns, len);
            }
            
            // Shrink window when we have more than k distinct characters
            if(mp.size() > k){
                // Decrease frequency of leftmost character
                mp[s[j]]--;
                
                // Remove character from map if frequency becomes 0
                if(mp[s[j]] == 0) {
                    mp.erase(s[j]);
                }
                
                // Move left pointer to shrink window
                j++;
            }
        }
        
        return maxAns;
    }
    
};