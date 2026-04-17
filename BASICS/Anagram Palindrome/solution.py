class Solution:
    def canFormPalindrome(self, s):
        # code here
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1 
        is_odd=0
        for val in freq.values():
            if val&1==1:
                is_odd+=1
        return is_odd<2