# Sliding Window Solution (O(n), O(1))

# 🔹 Problem
Find the length of the smallest substring that contains all characters '0', '1', and '2'.

# 💡 Approach (Sliding Window)

We use two pointers (left & right) to maintain a window:

Expand window using right

Track count of '0', '1', '2'

When all 3 are present → shrink window from left

Update minimum length