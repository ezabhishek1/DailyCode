# Approach Explanation: Segregate 0s and 1s
## Problem Understanding
The goal of the problem is simple: rearrange the array so that all 0s come first and all 1s come after that.

## My Thought Process
Instead of using swapping or trying to move elements around, I thought of a simpler way.

If I already know how many 0s are present in the array, then I can just place them directly in the beginning. After that, all remaining positions can be filled with 1s.

So I divided my approach into two steps.

### Step 1: Count the elements
Traverse the array once.

Count how many 0s are present.

(Counting 1s is optional for this logic, but I kept it for clarity.)

### Step 2: Modify the array
Traverse the array again using index.

For the first count_of_zeros indices → assign 0.

For the rest of the indices → assign 1.

This way, the array gets rearranged without worrying about the original positions.