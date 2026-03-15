Tree Portion Returning

DFS Traversal & Backtracking of UnOrdered HashMap that is passed by-reference

Problem K Sum Paths | Practice | GeeksforGeeks

Approach

Do the standard DFS Traversal and create a hashmap to identify and compare the correct subnodes sum. 

The only catch here is that if you don't pass the container by-reference you get a TLE, so pass container by-reference and don't forget to backtrack and decrease the node sum count in it. 

Time & Space Complexity

O(n) time (recursion) and space (Unordered Map), where n is the number of nodes.