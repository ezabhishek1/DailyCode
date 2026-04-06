class Solution {
  public:
    int dp[51][3000];
    int fun(vector<int>& arr, int t, int i, int sum){
        if(i==arr.size()){
            if(sum==t){return 1;}
            return 0;
        }
        if(dp[i][sum+1000]!=-1){return dp[i][sum+1000];}
        return dp[i][sum+1000]=fun(arr, t, i+1, sum+arr[i])+fun(arr, t, i+1, sum-arr[i]);
    }
    int totalWays(vector<int>& arr, int target) {
        memset(dp, -1, sizeof(dp));
        return fun(arr, target, 0, 0);
    }
 
};