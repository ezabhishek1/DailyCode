⭐ Problem: Maximum Chocolates Collected by Two Friends (Ninja and His Friends – DP-13)
You are given an n x m grid.
Two people start from:

Person A: starts at (0, 0)

Person B: starts at (0, m-1)

At each row, both can move to:

(j), (j-1), (j+1)
They move down together, and if both stand on the same cell, chocolate is counted only once.

Goal → maximize total chocolates collected.


✅ PART-1 | Memoization (Top-Down DP)
-----------------------------------------
Idea
Each state is encoded by:

(i, j1, j2)
i  → current row
j1 → column of person A
j2 → column of person B
Transitions
Both characters have 3 movement options:

dj1 = -1, 0, +1
dj2 = -1, 0, +1
Total 9 combinations:

(j1 + dj1, j2 + dj2)
If both land on the same cell → count chocolate once.
Else → add chocolates from both cells.

Memoize using a 3D array: dp[i][j1][j2].

⭐ Time & Space Complexity (Memoization)
Time:
There are m * n * n states → each tries 9 transitions
✔ O(m × n² × 9) = O(m × n²)

Space:
DP array: O(m × n × n)

Recursion stack: O(m)

✔ Space = O(m × n²)
