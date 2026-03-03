# Chocolate Distribution Problem

## Solution Approach

### Sliding Window on Sorted Array

1. **Sort the array** in ascending order
2. **Use a sliding window** of size m
3. **For every window**, calculate:
   - difference = arr[i + m - 1] - arr[i]
4. **Track the minimum** difference among all windows

## Key Insight: Why Sorting?

Sorting ensures that the minimum and maximum values in any chosen group of m packets are at the window boundaries. After sorting, the difference between the first and last element in a window of size m represents the unfairness factor.

## Complexity Analysis

### Time Complexity
**O(n log n)** due to sorting

### Space Complexity
**O(1)** - only constant extra space used  
