class Solution {
public:
    int smallestSubstring(string s) {
        int n = s.size();
        
        int c0 = 0, c1 = 0, c2 = 0;
        int l = 0, ans = INT_MAX;
        
        for(int r = 0; r < n; r++) {
            if(s[r] == '0') c0++;
            else if(s[r] == '1') c1++;
            else c2++;
            
            while(c0 > 0 && c1 > 0 && c2 > 0) {
                ans = min(ans, r - l + 1);
                
                if(s[l] == '0') c0--;
                else if(s[l] == '1') c1--;
                else c2--;
                
                l++;
            }
        }
        
        return ans == INT_MAX ? -1 : ans;
    }
};