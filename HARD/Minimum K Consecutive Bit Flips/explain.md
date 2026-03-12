Intuition behind sliding window and queue explained step by step in detail: https://youtu.be/Mxca8kfzWEk
Must Watch!!

O(N) time and O(k) space solution.


✅ Approach 1: Brute Force (Simulation)

Idea:

Traverse the array from left to right.

Whenever you see a 0, flip the next k bits manually (toggle them one by one).

Count the number of flips.

If at any point you need to flip but don’t have k elements left, return -1.

After finishing, if all elements are 1, return the count.