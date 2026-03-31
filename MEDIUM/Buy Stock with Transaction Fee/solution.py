class Solution:
    def maxProfit(self, arr, k):
        hold_y=-arr[0]
        hold_n=0
        for ix in range(1,len(arr)):
            hold_y,hold_n=max(hold_y,hold_n-arr[ix]),max(hold_y+arr[ix]-k,hold_n)
        return hold_n