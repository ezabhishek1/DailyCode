class Solution:
    
    def diagView(self, mat): 
        ans=[]
        n=len(mat)
        for i in range(1,n+1):
            for row in range(i):
                col=i-row-1
                ans.append(mat[row][col])
        for i in range(n-1,0,-1):
            for row in range(n-i,n):
                col=2*n-row-i-1
                ans.append(mat[row][col])
        return ans