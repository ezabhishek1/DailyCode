class Solution:
    def sortBySetBitCount(self, arr):
        # bin(x).count('1') returns the number of set bits
        # reverse=True ensures descending order
        arr.sort(key=lambda x: bin(x).count('1'), reverse=True)
        return arr