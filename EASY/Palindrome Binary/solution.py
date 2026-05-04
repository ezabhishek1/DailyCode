class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        
        binaryvalue=[]
        while n>0:
            binaryvalue.append(n%2)
            n=n//2
        
        m=len(binaryvalue)
        left=0
        right=m-1
        
        while left<right:
            if binaryvalue[left]!=binaryvalue[right]:
                return False
            left=left+1
            right=right-1
        return True
        