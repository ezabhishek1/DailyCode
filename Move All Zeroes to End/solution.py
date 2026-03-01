class Solution:
	 def pushZerosToEnd(self, arr):
        last_free = 0
        for a in arr:
            if a:
                arr[last_free] = a
                last_free += 1
        for i in range(last_free, len(arr)):
            arr[i] = 0