class Solution:
    def missingRange(self, arr, low, high):
        #code here
        from bisect import bisect_left
        arr.sort()
        ans = []
        for e in range(low, high+1):
            i = bisect_left(arr, e)
            if i >= len(arr) or arr[i] != e:
                ans.append(e)
        return ans