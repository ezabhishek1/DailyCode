Approach
Start with answer = 0.

Keep a variable len to store the current strictly increasing segment length.

Initially, len = 1 because one element alone is always a segment of length 1.

Traverse the array from index 1 to n-1.

If arr[i] > arr[i-1], then the increasing segment continues:

Increase len

Add len - 1 to the answer

Otherwise:

Reset len = 1

Return the final answer.


