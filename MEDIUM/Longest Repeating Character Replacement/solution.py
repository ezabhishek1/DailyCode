class Solution:
    def longestSubstr(self, s, k):
        n=len(s)
        freq={}
        maxFq=0
        l=0
        ans=0
        for r in range(n):
            freq[s[r]]=freq.get(s[r],0)+1
            maxFq=max(maxFq,freq[s[r]])
            while r-l+1-maxFq>k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            ans=max(ans,r-l+1)
        return ans