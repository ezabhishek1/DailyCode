class Solution:
     def subarrayXor(self, arr, k):
        # code here
        from collections import defaultdict
        d = defaultdict(int)
        d[0] = 1
        ans, running = 0, 0
        for e in arr:
            running ^= e
            sk = running^k
            if sk in d:
                ans += d[sk]
            d[running] += 1
        return ans