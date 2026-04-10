
The problem:
Find i < j < k s.t. arr[i] < arr[j] < arr[k].
Return these numbers in an array or list.

Let's understand some points: 
- Basically, we need to find a triplet s.t. above condition is true.
- It needs to be a subsequence not a subarray.
   So, the i, j, k need not be consecutive indices.  
- Other than finding if such a subsequence exists,
   we also have to return the numbers.
- For this same reason, we cannot solve the problem using 2 variables:
   first, second - which would hold smallest and second smallest numbers found so far.
   It takes O(n) time and O(1) auxiliary space.
   It always efficiently tells us if such a valid subsequence exists, 
   BUT it does not guarantee to return correct subsequence!
   So, we must find another way.