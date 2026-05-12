class Solution:
    def maxProfit(self, x, y, a, b):
        lth=len(a)
        tmp=sorted([(abs(va-vb),ix,) for ix,(va,vb,) in enumerate(zip(a,b))],reverse=True)
        ret=0
        for ix in range(lth):
            if(a[tmp[ix][1]]>b[tmp[ix][1]] or y<=0) and x>0:
                ret+=a[tmp[ix][1]]
                x-=1
            else:
                ret+=b[tmp[ix][1]]
                y-=1
        return ret

