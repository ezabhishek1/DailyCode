class Solution:
    def findKRotation(self, arr):
        # code here
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return i+1
        return 0