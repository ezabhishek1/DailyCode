# Approach Explanation: Segregate 0s and 1s
## Problem Understanding
The goal of the problem is simple: rearrange the array so that all 0s come first and all 1s come after that.

## My Thought Process
Instead of using swapping or trying to move elements around, I thought of a simpler way.

If I already know how many 0s are present in the array, then I can just place them directly in the beginning. After that, all remaining positions can be filled with 1s.
