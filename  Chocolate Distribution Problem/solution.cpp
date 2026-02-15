class Solution {
  public:
    int findMinDiff(vector<int>& a, int m) {
        // code here
        sort(a.begin(),a.end());
        
        int start = 0;
        int end = m-1;
        int ans = INT_MAX;
        
        while(end<a.size()){
            ans = min(ans,(a[end]-a[start]));
            start++;
            end++;
        }
        
        return ans;
    }
};