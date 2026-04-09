class Solution:
    def intersection(self,a, b):
        sol=[]
        i=0
        j=0
        s=set()
        while(i<len(a) and j<len(b)):
            if a[i]==b[j]:
                if a[i] not in s:
                    sol.append(a[i])
                    s.add(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else:
                j+=1
        return solx