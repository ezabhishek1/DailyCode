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

// Time Complexity: O(n * k) 
// Space Complexity: O(1)



✅ Approach 2: Optimized (Greedy + Sliding Window)

Idea:

Instead of flipping bits one by one, track flips using a sliding window.

A bit is “effectively 0” if it has been flipped an even number of times and “effectively 1” if flipped an odd times.

Maintain a queue (or difference array) to track active flips.

If the current bit is 0 (after considering active flips), we must start a new flip at this position.

If at any position i + k > n, return -1.

Code (Queue-based, O(k) space):

// Time Complexity: O(n)
// Space Complexity: O(k)