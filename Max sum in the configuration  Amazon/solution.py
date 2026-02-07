class Solution:
    def maxSum(self, arr):
        lth=len(arr)
        sm=sum(arr)
        cur=sum(ix*ve for ix,ve in enumerate(arr))
        mx=cur
        for ix in range(lth-1):
            cur+=sm-lth*arr[lth-1-ix]
            mx=max(mx,cur)
        return mx