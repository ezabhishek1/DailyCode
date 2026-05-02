class Solution:
    def findPosition(self, n: int) -> int:
        if n <= 0 or (n & (n - 1)) != 0:
            return -1
        return n.bit_length()