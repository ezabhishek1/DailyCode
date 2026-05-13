import math

class Solution:
    def RangeLCMQuery(self, arr, queries):
        n, seg = len(arr), [1]*(4*len(arr))
        lcm = lambda a,b: a*b//math.gcd(a,b)

        def build(i,l,r):
            if l==r: seg[i]=arr[l]; return
            m=(l+r)//2; build(i*2+1,l,m); build(i*2+2,m+1,r)
            seg[i]=lcm(seg[i*2+1],seg[i*2+2])

        def upd(i,l,r,p,v):
            if l==r: seg[i]=v; return
            m=(l+r)//2
            (upd(i*2+1,l,m,p,v) if p<=m else upd(i*2+2,m+1,r,p,v))
            seg[i]=lcm(seg[i*2+1],seg[i*2+2])

        def qry(i,l,r,L,R):
            if R<l or L>r: return 1
            if L<=l and r<=R: return seg[i]
            m=(l+r)//2
            return lcm(qry(i*2+1,l,m,L,R),qry(i*2+2,m+1,r,L,R))

        build(0,0,n-1)
        ans=[]
        for q in queries:
            if q[0]==1: upd(0,0,n-1,q[1],q[2])
            else: ans.append(qry(0,0,n-1,q[1],q[2]))
        return ans