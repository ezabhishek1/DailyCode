# Max Min Height

## Problem Overview

We have flowers in a row, and we can water w consecutive flowers each day for k days. When we water a flower, its height increases by 1. The goal is to **maximize the minimum height** among all flowers.

## Key Insight

This is a classic **binary search problem**! The key insight is:
- If we can achieve a minimum height of x, then we can also achieve any minimum height less than x
- This **monotonic property** makes binary search perfect here

## Solution Approach

### Binary Search + Greedy Strategy

1. **Binary Search Setup**: Set the search range from 0 to the maximum possible minimum height

2. **Greedy Checking**: For each candidate minimum height, use a greedy approach to check if it's achievable

3. **Greedy Strategy**: Always water the leftmost flower that hasn't reached the target height yet

4. **Sliding Window**: Use a sliding window of size w to efficiently track which flowers get watered

### Why This Works

The greedy strategy works because if we need to water a flower at position i, it's always optimal to place our watering window starting as early as possible while still covering position i.

## Complexity Analysis

### Time Complexity
**O(n log(max_height))** where n is the number of flowers and max_height is the maximum possible minimum height

### Space Complexity
**O(1)** - only a few extra variables for tracking