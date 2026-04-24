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
 
 ### Now, Total visible buildings = 4


# 2) Intuition
## The key idea is:

A building receives sunlight only if it is taller than all buildings to its left.

So instead of comparing each building with all previous ones (which is inefficient), we:

Keep track of the maximum height seen so far
For each building:
If current height >= max height → it is visible
Update max height

### This converts a potentially O(n²) problem into an O(n) solution.


# 3) Algorithm :

## Base Case

- If array has at least one building:
-- First building always gets sunlight
-- → initialize:
---- max_building_len_so_far = arr[0]
---count = 1

## Steps

- Initialize:
-- max_building_len_so_far = arr[0]
-- total_buildings = 1

-Traverse from index 1 to n-1:
-- If arr[i] > max_building_len_so_far :
-- total_buildings++
-- max_building_len_so_far = arr[i]

- Return total_buildings
 

# 4)Complexity Analysis:

## Time Complexity: O(n)

- Single traversal of array

## Space Complexity: O(1)

- No extra space used
- Where , n is the size of array


# 5) Dry Run:

## Input:
            arr = [6, 2, 8, 4, 11, 13]


