class Solution:
    def findMean(self, arr, queries):
        # code here
        ans = []
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i]
        
        for r in queries:
            Sum = prefix[r[1]] - (prefix[r[0] - 1] if r[0] > 0 else 0)
            ans.append(Sum // (r[1] - r[0] + 1))
        return ans