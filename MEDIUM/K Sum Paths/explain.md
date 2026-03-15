Tree Portion Returning

DFS Traversal & Backtracking of UnOrdered HashMap that is passed by-reference

Problem K Sum Paths | Practice | GeeksforGeeks

Approach

Do the standard DFS Traversal and create a hashmap to identify and compare the correct subnodes sum. 

The only catch here is that if you don't pass the container by-reference you get a TLE, so pass container by-reference and don't forget to backtrack and decrease the node sum count in it. 

Time & Space Complexity

O(n) time (recursion) and space (Unordered Map), where n is the number of nodes.



🔥 Intuition
The goal is to find the number of paths in a binary tree where the sum of the node values equals k. Instead of checking all possible paths in a brute-force manner, we use a prefix sum approach to efficiently count valid paths while traversing the tree.

🚀 Approach
Use a HashMap (prefixSum) to store the cumulative sum of node values along a path.
Perform a Depth-First Search (DFS) while maintaining the current sum.
Check how many times (currentSum - k) has appeared in prefixSum, as this indicates the presence of a valid path.
Recursively traverse the left and right subtrees, updating prefixSum accordingly.
Backtrack after visiting each node to ensure it doesn't affect other paths.
⏳ Complexity
Time Complexity: O(N), as each node is visited once.
Space Complexity: O(H), where H is the height of the tree (best case O(log⁡N), worst case O(N).