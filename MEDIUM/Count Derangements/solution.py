class Solution:
    def derangeCount(self, n: int) -> int:
        if n==1:
            return 0
        
        if n==2:
            return 1
        
        dp = [0]*(n+1)
        
        dp[1] = 0
        dp[2] = 1
        
        for i in range(3,n+1):
            dp[i] = (i-1)*(dp[i-1]+dp[i-2])
        
        return dp[n]