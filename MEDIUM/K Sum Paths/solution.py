class Solution:
    def countAllPaths(self, root, k):
        ret=cur=0
        from collections import defaultdict
        prv=defaultdict(int)
        prv[0]=1
        def bt(node=root):
            nonlocal k,ret,cur,prv
            if not node:
                return
            cur+=node.data
            if cur-k in prv:
                ret+=prv[cur-k]
            prv[cur]+=1
            bt(node.left)
            bt(node.right)
            prv[cur]-=1
            cur-=node.data
        bt()
        return ret