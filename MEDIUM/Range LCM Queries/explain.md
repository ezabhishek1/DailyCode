Approach
I used a Segment Tree where every node stores the LCM of a range.

Steps:

Build the segment tree

Leaf node stores the array value.

Internal node stores LCM of left child and right child.

For update query [1, index, value]

Move to that index in the tree.

Replace old value with new value.

Recalculate LCM while returning back.

For range query [2, L, R]

Traverse only the required segments.

Combine answers using LCM.

I also used GCD while calculating LCM because:

![alt text](e0795266-74e9-46c4-8d93-099e2d94db16_1778554308.png)