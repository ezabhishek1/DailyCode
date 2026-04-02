int mod=1000000007;
class Solution{
    public:
    long long util(int n,bool flag,int k,vector<vector<long long>> &dp){
        if(n==0) return 1;
        if(dp[n][flag]!=-1) return dp[n][flag];
        long long ans=1;
        if(flag){
            ans=(ans*((k-1)*util(n-1,false,k,dp))%mod)%mod;
        }
        else{
            ans=(ans*((1*util(n-1,true,k,dp)+((k-1)*util(n-1,false,k,dp))%mod)%mod))%mod;
        }
        return dp[n][flag]=ans;
    }
    long long countWays(int n, int k){
        // code here
        vector<vector<long long>> dp(n+1,vector<long long>(2,-1));
        return (k*util(n-1,0,k,dp))%mod;
    }
};