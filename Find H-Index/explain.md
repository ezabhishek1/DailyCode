# H-Index Problem

## Problem Statement
The H-Index is a metric that measures the productivity and citation impact of a researcher. A researcher has index h if h of their N papers have at least h citations each, and the remaining papers have no more than h citations.

Given an array of citation counts for papers, determine the maximum H-Index value.

## Approaches

### Approach 1: Sorting (C++ Solution)
**Algorithm:**
1. Sort citations in descending order
2. Iterate through sorted citations
3. At index i, if citations[i] >= i+1, then h-index could be i+1
4. Return the maximum h-index found

**Time Complexity:** O(n log n) - dominated by sorting
**Space Complexity:** O(1) - ignoring the sorting space

### Approach 2: Counting (Python Solution)
**Algorithm:**
1. Create a count array of size n+1 (since h-index can't exceed n)
2. Iterate through citations:
   - If citation >= n, increment count[n]
   - Else increment count[citation]
3. Traverse count array from right to left, accumulating totals
4. Return the first index i where total >= i

**Time Complexity:** O(n) - linear traversal and counting
**Space Complexity:** O(n) - for the count array

## Use Cases

### When to use Approach 1 (Sorting):
- Simple and intuitive logic
- When sorting overhead is acceptable
- Smaller datasets (n < 10^4)
- When code clarity is prioritized over optimization
- Interview scenarios where explaining the logic matters more than optimization

### When to use Approach 2 (Counting):
- Large datasets (n > 10^4) where O(n) beats O(n log n)
- Performance-critical applications requiring optimal complexity
- When you need guaranteed linear time complexity
- Memory available for count array

## Key Insights
- The h-index is bounded: it can never exceed the number of papers (n)
- Using a counting approach avoids the expensive sorting operation
- The counting approach leverages the fact that h-index has a limited range [0, n]

## Examples

**Example 1:**
- Input: citations = [25, 8, 5, 3, 3]
- Sorted: [25, 8, 5, 3, 3]
- At i=0: citations[0]=25 >= 1 ✓
- At i=1: citations[1]=8 >= 2 ✓
- At i=2: citations[2]=5 >= 3 ✓
- At i=3: citations[3]=3 >= 4 ✗
- Output: h-index = 3

**Example 2:**
- Input: citations = [100, 100, 100, 100]
- Output: h-index = 4 (all 4 papers have >= 4 citations)

## Comparison Table

| Aspect | Sorting | Counting |
|--------|---------|----------|
| Time Complexity | O(n log n) | O(n) |
| Space Complexity | O(1) | O(n) |
| Best for | Simplicity | Large datasets |
| Readability | High | Medium |
| Implementation | Straightforward | Slightly tricky |
