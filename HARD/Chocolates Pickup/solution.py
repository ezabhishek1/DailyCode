from math import inf
from itertools import product

class Solution:
    def maxChocolate(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [[[-inf for k in range(m+2)] for j in range(m+2)] for i in range(n)]
        dp[0][1][m] = grid[0][0] + (grid[0][m-1] if m>1 else 0)
        
        for i in range(1, n):
            for j in range(1, m+1):
                for k in range(1, m+1):
                    cur = grid[i][j-1] + (grid[i][k-1] if j!=k else 0)
                    dp[i][j][k] = cur + max(dp[i-1][nj][nk] for nj,nk in product([j-1, j, j+1], [k-1, k, k+1]))
                                    
        return max(map(max, dp[-1]))