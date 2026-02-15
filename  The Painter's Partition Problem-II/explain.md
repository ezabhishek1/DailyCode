# The Painter's Partition Problem-II

## Problem Overview

We are given an array where each element represents the time required for a job. We have k workers and each worker can do only continuous jobs. Our goal is to **minimize the maximum time** taken by any worker.

## Key Insight

This problem is solved using **Binary Search on Answer**.

The key insight is: if we can partition jobs such that the maximum time is at most x, then we can also do it with any value greater than x. This monotonic property makes binary search suitable.

## Solution Approach

### Binary Search Setup

- **Low**: Maximum element in the array (minimum possible answer - at least one worker takes the longest job)
- **High**: Sum of all elements (maximum possible answer - one worker does all jobs)

### Helper Function: Can We Achieve Maximum Time of `mid`?

The function `helper(arr, mid, k)` checks whether it's possible to divide the jobs into k or fewer workers such that no worker gets more than `mid` time.

**Algorithm:**
1. Initialize `sumi = 0` (current worker's total time) and `count = 0` (workers used)
2. Iterate through each job:
   - Add job time to `sumi`
   - If `sumi > mid`, assign this job to a new worker (reset `sumi` to current job time)
   - Increment worker `count`
3. If `count <= k`, return true (achievable); else return false

### Main Binary Search Loop

1. While `low <= high`:
   - Calculate `mid = (low + high) / 2`
   - If `helper(arr, mid, k)` returns true: we can achieve this, try to minimize further (`high = mid - 1`, store in `ans`)
   - If helper returns false: increase the search space (`low = mid + 1`)
2. Return `ans` as the minimum time required

## Complexity Analysis

### Time Complexity
**O(n log(sum of array))** where n is the number of jobs

### Space Complexity
**O(1)** - only constant extra space used

