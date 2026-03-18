# Problem Statement

Given a non-negative integer represented as a non-empty array of digits, you may replace one digit with any other digit (0-9). Return the largest possible number you can get after making at most one swap.

# Approach & Intuition

1. **Identify the Maximum Digit**: Traverse the array from right to left to identify the maximum digit and its index.
2. **Find the Swap Candidate**: Traverse the array from left to right to find the first digit that is smaller than the maximum digit identified in the previous step.
3. **Perform the Swap**: Swap the identified digit with the maximum digit.
4. **Return the Result**: Convert the array back to an integer and return it.

# Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the array. We traverse the array twice.
- **Space Complexity**: O(1), as we are using a constant amount of extra space.

# Example Walkthrough

Consider the input array `[9, 4, 9, 8, 3]`.

1. Traverse from right to left to identify the maximum digit and its index:
   - Maximum digit is `9` at index `0`.
2. Traverse from left to right to find the first digit smaller than the maximum digit:
   - The first digit smaller than `9` is `4` at index `1`.
3. Swap `4` and `9`:
   - Resulting array is `[9, 9, 4, 8, 3]`.
4. Convert the array back to an integer:
   - The largest number possible is `99483`.

# Code Implementation