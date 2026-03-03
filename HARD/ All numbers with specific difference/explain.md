# All Numbers with Specific Difference

## Problem Overview

Find all numbers up to n where the difference between the number and the sum of its digits equals a specific value d.

## Key Insight

The crucial observation is that **a number is always greater than the sum of its digits**.

Once we find the smallest number that satisfies the condition, all numbers greater than it (up to n) will also satisfy the condition. This monotonic property makes binary search the ideal approach.

## Solution Approach

### Using Binary Search

1. **Search Range**: Find the lowest number that satisfies the condition (number - sum of digits ≥ d)

2. **Binary Search on Answer**: Eliminate half of the possible answers in each iteration to find the minimum number satisfying the condition

3. **Count Valid Numbers**: Once the lowest number is found, count all numbers between it and n

### Edge Case

If n is less than 10, then the difference between any number and the sum of its digits is 0. In this case:
- If d is not equal to 0, the minimum valid number is greater than n, so return 0
- Otherwise, count numbers that satisfy the condition

## Complexity Analysis

### Time Complexity
**O(log n)** - The outer binary search loop runs O(log n) times, and for each number, we calculate the digit sum which takes at most 9 operations (for numbers up to 10^9)

### Space Complexity
**O(1)** - only constant extra space used
