# Equalize the Towers

## Solution Approach

### Binary Search for Convex Function

In the C++ version of the solution, we use a **very simple solution using Binary Search** for a convex function.

## Key Concept

### Does the Cost Function Form a Convex "V"?

**Yes**, the cost function forms a convex "V" shape.

## Proof

The cost function is convex because:

1. **Definition**: The cost function is the sum of absolute differences between each tower height and a target height.

2. **Mathematical Property**: The sum of absolute value functions is convex.
   - Each term `|height[i] - target|` is a convex function (V-shaped)
   - The sum of convex functions is convex

3. **Implication**: This means:
   - There is a **single global minimum**
   - The function decreases as we move toward the optimal height
   - Binary search can efficiently find this minimum

### Why Binary Search Works

Because the cost function is convex (unimodal), binary search can efficiently find the minimum cost by:
- Eliminating half the search space in each iteration
- Time Complexity: **O(log(max_height) * n)**