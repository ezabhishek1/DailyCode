# Approach
- Count total number of 1s → k

- If k == 0, return -1 (no 1s present)

- Use a sliding window of size k

- Count number of 1s inside current window

- Track maximum number of 1s in any window

- Minimum swaps = k - max_ones_in_window


# Why?

Because remaining elements in window are 0s → those need swapping