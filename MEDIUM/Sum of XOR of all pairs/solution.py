class Solution:
    def sumXOR(self, arr):
        n = len(arr)

        # If only one element, no pair exists
        if n < 2:
            return 0

        ans = 0

        # Check each bit position (0 to 31)
        for bit in range(32):
            count_set = 0

            # Count elements with current bit set
            for num in arr:
                if num & (1 << bit):
                    count_set += 1

            count_unset = n - count_set

            # Contribution of this bit
            ans += count_set * count_unset * (1 << bit)

        return ans