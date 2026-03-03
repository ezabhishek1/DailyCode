class Solution {
  public:
    int maxProfit(vector<int> &prices) {
        int mini=100000;
        int ans=0;
        for(auto x:prices)
        {
            mini=min(mini,x);
            ans=max(ans,x-mini);
        }
        return ans;
    }
};