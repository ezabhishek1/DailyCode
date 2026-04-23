# Problem Statement:
Given an array of integers arr, return true if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays are equal. If it is not possible then return false.

# APPROACH:

- Step 1: Calculate Total Sum: First, calculate the total sum of all the elements in the array.
- Step 2: Initialize Partial Sum: Initialize a variable partialSum to keep track of the sum of elements from the right end of the array.
- Step 3: Iterate from Right to Left: Iterate through the array from the last element to the first.
-- In each iteration:
--- Add the current element to partialSum.
--- Subtract the current element from totalSum (effectively splitting the array into two parts: the part on the right contributing to partialSum, and the part on the left contributing to totalSum).
-- Check if partialSum equals totalSum. If they are equal, it means the array can be split into two subarrays with equal sums, so return true.
- Step 4: Return False if No Split Found: If no such split is found after the loop, return false.

# Time Complexity: 
- The algorithm runs in O(n) time, where n is the size of the array. This is because we traverse the array twice (once to calculate the total sum and once to find the split point).

# Space Complexity: 
- The algorithm uses O(1) space, as it only requires a few additional variables.


# DRY RUN:

Let's dry run the solution using the first example:

## Input: arr = [1, 2, 3, 4, 5, 5]

- Step 1: Calculate the total sum of the array:

totalSum = 1 + 2 + 3 + 4 + 5 + 5 = 20
-
- Step 2: Initialize partialSum to 0:

partialSum = 0

- Step 3: Start iterating from the last element to the first:

-- Iteration 1 (i = 5):
--- partialSum = 0 + 5 = 5
--- totalSum = 20 - 5 = 15
--- partialSum != totalSum
-- Iteration 2 (i = 4):
--- partialSum = 5 + 5 = 10
--- totalSum = 15 - 5 = 10
---partialSum == totalSum, so return true.


## Output: The function returns true, which is correct.