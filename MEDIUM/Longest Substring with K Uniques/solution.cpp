class Solution {
  public:
    int longestKSubstr(string &s, int k) {
        // code here
        unordered_map<char,int> mp;
        int maxAns=-1;
        // traverse on the string
        int j=0;
        for(int i=0;i<s.length();i++){
            mp[s[i]]++;
        // calculate max value if we have excatly k distinct character
            if(mp.size()==k){
                int len=i-j+1;
                maxAns=max(maxAns,len);
            }
            // shrink window only if size of map is greater than k
            if(mp.size()>k){
                // remove value at jth pos
                mp[s[j]]--;
                if(mp[s[j]]==0) mp.erase(s[j]);
                j++;
                
            }
        }
        return maxAns;
    }
    
};