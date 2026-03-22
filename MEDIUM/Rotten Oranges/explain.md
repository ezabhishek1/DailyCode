Approach:
1. Traverse the matrix:
   - Add all rotten oranges (value=2) to a queue with time = 0.
   - Count the number of fresh oranges (value=1).

2. Perform BFS:
   - At each step, pop a rotten orange from the queue.
   - For each of its 4 neighbors (up, down, left, right):
     - If the neighbor is fresh, rot it (set to 2), decrement fresh count, and push it into the queue with time+1.

3. Track the maximum time during BFS.

4. If fresh oranges remain at the end → return -1.  
   Otherwise → return the maximum time.
   