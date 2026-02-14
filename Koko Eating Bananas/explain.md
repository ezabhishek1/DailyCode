# Koko Eating Bananas

## Problem Overview

- Koko can eat only **1 pile in 1 hour**
- He can eat either the entire pile or some bananas from a pile in 1 hour
- **Goal**: Find the minimum eating speed so all piles are finished within `k` hours

## Key Constraints

### Maximum Speed
- **Speed**: Equal to the largest pile size (`hi`)
- **Result**: Time taken = number of piles (array length)

### Minimum Speed
- **Speed**: 1 banana per hour (`lo`)
- **Result**: Time taken = total bananas across all piles

## Solution Approach

**Binary Search** on all possible speeds from `1` to `hi`

### Why Binary Search?
- As speed increases, time decreases (monotonic relationship)
- We need to find the minimum viable speed that satisfies the constraint
- Search space is continuous from 1 to max pile size