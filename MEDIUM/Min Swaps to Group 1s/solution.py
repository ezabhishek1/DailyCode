class Solution:
     def minSwaps(self, arr):
        n = len(arr)
        ones = arr.count(1)
        if ones == 0:
            return -1
        if ones == n:
            return 0
        window = max_ones = sum(arr[:ones])
        for i in range(ones, n):
            window += arr[i] - arr[i - ones]
            if window > max_ones:
                max_ones = window
        return ones - max_ones