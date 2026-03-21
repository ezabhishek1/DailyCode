class Solution:
    
    numBST=[]
    
    @classmethod
    def computeNumBST(cls):
        Solution.numBST=[0]*7
        Solution.numBST[0]=1
        Solution.numBST[1]=1
        for i in range(2,7):
            for j in range(1,i+1):
                small=j-1
                large=i-j
                Solution.numBST[i]+=Solution.numBST[small]*Solution.numBST[large]

    def countBSTs(self, arr):
        if not Solution.numBST:
            Solution.computeNumBST()
        l=[(x,i) for i,x in enumerate(arr)]
        l.sort()
        n=len(arr)
        ans=[None]*n
        for i in range(1,len(arr)+1):
            ans[l[i-1][1]]=Solution.numBST[i-1]*Solution.numBST[n-i]
        return ans
        