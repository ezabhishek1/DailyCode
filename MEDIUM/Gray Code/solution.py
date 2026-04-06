class Solution:
    def graycode(self,n):
        gc=['0','1']
        def recur(n=n-1):
            nonlocal gc
            if n==0:
                return
            gc+=gc[::-1]
            m=len(gc)//2
            for ix in range(m):
                gc[ix]='0'+gc[ix]
                gc[ix+m]='1'+gc[ix+m]
            recur(n-1)
        recur()
        return gc

