# Approach
- I create a prefix sum array of size n + 1.

- prefix[i] stores the sum of first i elements.

- For every query [l, r]:

-- Find the range sum using prefix sum.

-- Find the length of the range using r - l + 1.

-- Divide sum by length.

-- Store the floor value of the mean in the answer array.

- Return the final answer array.

