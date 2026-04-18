# 1.Approach: Kadane’s Algorithm (Optimal)

convert the given array elements i.e 1  to -1 and 0 to 1
then apply the Kaden's algorithm
But before that store the currrent counts of ones

# 2. Algorithm
- Preprocessing & Counting: Iterate through the array.

-- Count the existing 1s (oneCnt).

-- Transform the array: Replace 0 with 1 and 1 with -1.

- Maximum Subarray Sum (Kadane's): Run Kadane’s algorithm on the transformed array to find the maximum possible gain (ans).

- Result: The final answer is the original number of 1s plus the maximum gain: oneCnt + ans.

# 3. Example Walkthrough
- Input: [1, 0, 0, 1, 0]

-- Original 1s: 2

-- Transformed Array: [-1, 1, 1, -1, 1]

-- Max Subarray Sum (Kadane's): 2 (from subarray [1, 1])

-- Result: 2 + 2 = 4

# 4. Complexity Analysis
- Time Complexity: O(N)

- We traverse the array twice (once for transformation/counting and once for Kadane’s). This results in linear time.

Space Complexity: O(1)

## The Input will be : ------   

10
1 0 0 1 1 0 0 0 1 0
