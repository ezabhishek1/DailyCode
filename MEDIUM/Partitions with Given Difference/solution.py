class Solution:
      def countPartitions(self, arr, diff):
     
        s = sum(arr)
        n = len(arr)
        if (s-diff)&1 != 0 or s < diff:
            return 0
        s = (s-diff)//2
 
        dp = [[0]*(n+1) for _ in range(s+1)]
       #  dp[0] = [1]*(n+1) this is wrong initialization when there is element that is 0
        dp[0][0] = 1
            
        
        for k in range(0, s+1): # sum has to start from 0 to count for element with 0 value
            for i in range(n):
                dp[k][i+1] = dp[k][i]
                if k-arr[i] >= 0:
                    dp[k][i+1] += dp[k-arr[i]][i]
                    
        return dp[-1][-1]