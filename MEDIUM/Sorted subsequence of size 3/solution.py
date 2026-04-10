class Solution:
    def find3Numbers(self, arr):
        maxa=[]
        mina=[]
        n=len(arr)
        for i in range(n):
            if i==0:
                mina.append(arr[i])
                maxa.append(arr[n-i-1])
            else:
                mina.append(min(mina[-1],arr[i]))
                maxa.append(max(maxa[-1],arr[n-i-1]))
        for i in range(n):
            if mina[i]<arr[i] and arr[i]<maxa[n-i-1]:
                return [mina[i],arr[i],maxa[n-i-1]]
        return []