class Solution:
    def countIncreasing(self, arr):
        # code here.
        i=1
        j=0
        ans=0
        while(i<len(arr)):
            if arr[i]>arr[i-1]:
                if i>j:
                    ans+=(i-j)
            else:
                j=i
            i+=1
        return ans