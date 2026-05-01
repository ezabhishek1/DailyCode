class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)

        # Check all parent nodes
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2

            # Check left child
            if left < n and arr[i] < arr[left]:
                return False

            # Check right child
            if right < n and arr[i] < arr[right]:
                return False

        return True