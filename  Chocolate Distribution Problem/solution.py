class Solution:
    def findMinDiff(self, arr, M):
        """
        Returns the minimum difference between the maximum
        and minimum chocolates among M selected packets.
        """

        n = len(arr)

        # Edge case: not enough packets
        if M == 0 or n < M:
            return 0

        # Sort packet sizes
        arr.sort()

        min_diff = float('inf')

        # Sliding window of size M
        for left in range(n - M + 1):
            right = left + M - 1
            diff = arr[right] - arr[left]
            min_diff = min(min_diff, diff)

        return min_diff