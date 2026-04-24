# #Buildings with Sunlight – Solution Explanation

# 1) Understanding the Problem :

## Consider the input:

      arr = [6, 2, 8, 4, 11, 13]

Sunlight comes from the left side.
A building can see sunlight only if no taller building exists to its left.
If a taller building exists on the left, it blocks sunlight for smaller buildings on the right.


## Step-by-step observation:
6 → first building → always gets sunlight
2 → shorter than 6 → blocked
8 → taller than all previous (6) → visible
4 → shorter than 8 → blocked
11 → taller than all previous → visible
13 → taller than all previous → visible
 