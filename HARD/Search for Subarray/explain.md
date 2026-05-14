# This question is fully based on KMP Algorithm


Approach
I treated array b as the pattern and array a as the main array where I need to search.

First, I built the LPS array for b.

LPS[i] stores the length of the longest proper prefix which is also a suffix for the subarray ending at index i.

This array helps me know where to continue matching if a mismatch happens.

Then I started comparing elements of a and b using two pointers:

i for array a

j for array b

Cases:

If a[i] == b[j]

Move both pointers forward.

If the whole pattern matches

Store the starting index.

Use LPS to continue searching for the next match.

If mismatch happens

If j != 0, move j using LPS.

Otherwise move i.

This way, every element is processed efficiently without unnecessary comparisons.