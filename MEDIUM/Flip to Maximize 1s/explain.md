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

# The Input will be : ------   

10
1 0 0 1 1 0 0 0 1 0

# [EXPLANATION ]

- Everytime we get 1, we increment oneCount to keep track of all ones.
- If we get 0, we can potentially convert it to 1. So ans++ as we have converted zero to one.
- Now, it may be possible we get max number of 1's by flipping 1 to 0.
- For ex, 01001000   here we flip all numbers from index 2 to 7.
- So, in case we get a 1, we decrement our ans, becoz by flipping it we reduced our number of ones.
- But, as you can see it is decreasing our ans, so to balance that
- At the end, we return oneCount+ans.
### Time Complexity of O(n) and Space Complexity of O(1).




first states for one, zero, & max

ONE=0	ZERO=0	 	MXi=0	 
Now RUN the Loop	< ONE >	< ZERO >	 	
 <MXi>

MXi=max(ZERO,MXi)

 
 	1	-1	 	  0	 
 	1	1	 	1	 
 	1	2	 	2	 
 	2	1	 	2	 
 	3	0	 	2	 
 	3	1	 	2	 
 	3	2	 	2	 
 	3	3	 	3	 
 	4	2	 	3	 
 	4	3	 	3	 
 	 	 	 	 	 
After runing	the loop	 we got	 	 this result.....	 
 	 	 	 	 	 
At the end =====	 one=4	     &	 	 max=3	 
 	 	 	 	 	 
 	The answer =	(one+max)	 	 7 (Correct)[out put]	 
 	 	 	 	 
