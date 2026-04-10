
## The problem:
Find i < j < k s.t. arr[i] < arr[j] < arr[k].
Return these numbers in an array or list.

## Let's understand some points: 
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



   ### Some thoughts:
- If we go for each element (curr idx = i) and find its j and k later in the array,
   it would result in a O(n^3) time solution. Not working... 
- What if... we focus on j instead?
- Think. Can we find the i and k for each j?
- If we can do this, we find our triplet, right?
- So, HOW to find 
   the i (which must lie on the left) and 
   the k (which must lie on the right)
   of our current j?

- We use 2 arrays:
smaller[j]: index of a smaller element to the left of arr[j] (or -1 if none).
--Find min seen so far.
greater[j]: index of a greater element to the right of arr[j] (or -1 if none).
--Find max seen so far.

## To find the valid subsequence, 
just check which element in our array has got a smaller element on left and a greater element on right.
Which is same as "check which j has +ve smaller[j] and a +ve greater[j]".
Our answer becomes -> {smaller[j], arr[j], greater[j]} !!!

### Note that:
- smaller[0] is always -1
- greater[last idx] is always -1