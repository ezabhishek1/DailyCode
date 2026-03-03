class Solution:
    def canAttend(self,arr):
        # Your Code Here
        arr.sort(key=lambda i: i[0])
        for i in range(1,len(arr)):
            i1 = arr[i-1]
            i2 = arr[i]
            if i1[1] > i2[0]:
                return False
        return True