
# Subarrays with First Element Minimum

## 📋 Problem Statement
Given an integer array `arr[]`, count the number of **subarrays** where the **first element** is the **minimum element** of that subarray.

> **Note**: A subarray is valid if its first element is **not greater than** any other element in that subarray.

### Examples

**Example 1:**
```
Input: arr[] = [1, 2, 1]
Output: 5

All possible subarrays:
[1], [1,2], [1,2,1], [2], [2,1], [1]

Valid subarrays (first element is minimum):
[1] → min = 1 ✓
[1,2] → min = 1 ✓
[1,2,1] → min = 1 ✓
[2] → min = 2 ✓
[2,1] → min = 1 (first element 2 is NOT minimum) ✗
[1] → min = 1 ✓

Total valid = 5
```

**Example 2:**
```
Input: arr[] = [1, 3, 5, 2]
Output: 8

Valid subarrays:
[1], [1,3], [1,3,5], [1,3,5,2], [3], [3,5], [5], [2]
Total = 8
```

### Constraints
- 1 ≤ arr.size() ≤ 5×10⁴
- 1 ≤ arr[i] ≤ 10⁵
- Expected Time Complexity: **O(n)**
- Expected Space Complexity: **O(n)**

---

## 🧠 Approach & Intuition

### Key Insight
For any element at index `i`, we need to find **how many subarrays starting at i** have `arr[i]` as the minimum.

**Observation**: A subarray starting at `i` will be valid **UNTIL** we encounter an element **smaller than arr[i]** to its right. Once we find a smaller element, any subarray extending beyond that point would have that smaller element, making `arr[i]` no longer the minimum.

### Mathematical Formulation

For element at index `i`:
1. Find the **next smaller element** to the right (at index `j`)
2. All subarrays starting at `i` that end **before** `j` are valid
3. Number of valid subarrays starting at `i` = `j - i`
   - End indices: i, i+1, i+2, ..., j-1
   - That's exactly `(j - i)` subarrays

If there's **no smaller element** to the right, then `j = n` (array length), and valid subarrays = `n - i`

---

## 🚀 Efficient Solution Using Stack (O(n))

### Algorithm
1. Use a **monotonic stack** (increasing) to find the **next smaller element** for each index
2. For each index `i` with next smaller at `j`, add `(j - i)` to result
3. Sum all counts

### Implementation

```python
def countSubarrays(arr):
    n = len(arr)
    ans = 0
    stack = []  # Stack stores indices
    
    for i in range(n):
        # Maintain increasing stack (pop when we find a smaller element)
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            # For idx, i is the next smaller element
            result += (i - idx)  # Valid subarrays starting at idx
        stack.append(i)
    
    # Process remaining indices (no smaller element to the right)
    while stack:
        idx = stack.pop()
        result += (n - idx)  # Can extend to end of array
    
    return result
```

### Dry Run with Example

Let's trace through step by step:

- **Initial State:** `n = 3`, `result = 0`, `stack = []`(empty)

**Iteration i = 0 (arr[0] = 1)**

| Step | Action | Code | Stack (indices) | result |
|---|--------|------|-----------------|--------|
| 1 | Stack empty? Yes, `arr[-1]=0` > `arr[0]=1` ✗ | `while stack and ...` | `[]` | 0 |
| 2 | Push current index i=0 | `stack.append(i)` | `[0]` | 0 |

**Iteration i = 1 (arr[1] = 2)**

| Step | Action | Code | Stack (indices) | result |
|---|--------|------|-----------------|--------|
| 3 | Check while: stack not empty ✓, arr[0]=1 > arr[1]=2? ✗ | `while stack and ...` | `[0]` | 0 |
| 4 | Push current index i=1 | `stack.append(i)` | `[0, 1]` | 0 |

---

**Iteration i = 2 (arr[2] = 1)**

| Step | Action | Code | Stack (indices) | result |
|---|--------|------|-----------------|--------|
| 5 | Check while: stack not empty ✓, arr[1]=2 > arr[2]=1 ✓ | `while stack and ...` | `[0, 1]` | 0 |
| 6 | Pop top index (1) | `idx = stack.pop()` | `[0]` | 0 |
| 7 | Add to result: i - idx = 2 - 1 = 1 | `result += (i - idx)` | `[0]` | **1** |
| 8 | Continue while: stack not empty ✓, arr[0]=1 > arr[2]=1 ✗ | | `[0]` | 1 |
| 9 | Push current index i=2 | `stack.append(i)` | `[0, 2]` | 1 |

---

**After Loop - Process Remaining Stack**

| Step | Action | Code | Stack (indices) | result |
|---|--------|------|-----------------|--------|
| 10 | Stack not empty ✓ | `while stack:` | `[0, 2]` | 1 |
| 11 | Pop top (2) | `idx = stack.pop()` | `[0]` | 1 |
| 12 | Add: n - idx = 3 - 2 = 1 | `result += (n - idx)` | `[0]` | **2** |
| 13 | Stack not empty ✓ | `while stack:` | `[0]` | 2 |
| 14 | Pop top (0) | `idx = stack.pop()` | `[]` | 2 |
| 15 | Add: n - idx = 3 - 0 = 3 | `result += (n - idx)` | `[]` | **5** |
| 16 | Stack empty → exit while | | `[]` | 5 |

**Final Result**
```
result = 5
```

✅ **Matches expected output!**

---

## 📊 **Visual Summary Table**

| Step | i | arr[i] | Stack Before | Action | Stack After | result |
|------|---|--------|--------------|--------|-------------|--------|
| 1 | 0 | 1 | [] | Push 0 | [0] | 0 |
| 2 | 1 | 2 | [0] | arr[0]=1 < 2 → Push 1 | [0,1] | 0 |
| 3 | 2 | 1 | [0,1] | Pop 1 → +1, Stop (1 not > 1) | [0,2] | 1 |
| 4 | End | - | [0,2] | Pop 2 → +1 | [0] | 2 |
| 5 | End | - | [0] | Pop 0 → +3 | [] | **5** |

---

## 🔄 **How Each Index Contributes**

| Index | Value | Next Smaller | Calculation | Contribution | Valid Subarrays |
|-------|-------|--------------|-------------|--------------|-----------------|
| 0 | 1 | None | n - 0 = 3 | **3** | [1], [1,2], [1,2,1] |
| 1 | 2 | at i=2 | 2 - 1 = 1 | **1** | [2] |
| 2 | 1 | None | n - 2 = 1 | **1** | [1] |
| **Total** | | | | **5** | |

---

## ✅ **Verification - All Valid Subarrays**

| Subarray | First Element | Minimum | Valid? |
|----------|---------------|---------|--------|
| [1] | 1 | 1 | ✓ |
| [1,2] | 1 | 1 | ✓ |
| [1,2,1] | 1 | 1 | ✓ |
| [2] | 2 | 2 | ✓ |
| [2,1] | 2 | 1 | ✗ |
| [1] (last) | 1 | 1 | ✓ |

**Count ✓ = 5** ✓

---

The algorithm correctly counts **5** valid subarrays where the first element is the minimum! 🎯
**Example**: `arr = [1, 2, 1]`


---

## 📊 Complexity Analysis

| Metric | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | **O(n)** | Each element pushed once, popped once |
| **Space** | **O(n)** | Stack can hold up to n elements |

---

## 🧪 Edge Cases

| Case | Input | Expected | Explanation |
|------|-------|----------|-------------|
| **Single element** | [5] | 1 | Only [5] |
| **All equal** | [2,2,2] | 3 | Each element: [2], [2], [2] (length 1 only) |
| **Strictly increasing** | [1,2,3,4] | 4 | Each element alone: [1], [2], [3], [4] |
| **Strictly decreasing** | [4,3,2,1] | 10 | 4+3+2+1 = 10 (each can extend to end) |

---

## 📝 Alternative Approaches

### 1. Brute Force (O(n²)) - Too Slow
```python
def brute_force(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        min_so_far = arr[i]
        for j in range(i, n):
            if arr[j] < min_so_far:
                break
            if arr[i] == min_so_far:
                count += 1
    return count
```
❌ **Problem**: O(n²) is too slow for n = 50,000

### 2. Using Next Smaller Element Array
```python
def with_nse_array(arr):
    n = len(arr)
    nse = [n] * n  # Initialize with n (array length)
    stack = []
    
    # Find next smaller element for each index
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            nse[idx] = i
        stack.append(i)
    
    # Sum up valid subarrays
    return sum(nse[i] - i for i in range(n))
```

---

## 🎯 Key Takeaways

1. **Monotonic Stack** is the key to solving "next smaller element" problems in O(n)
2. For each element, we only need to find the **first smaller element** to its right
3. **Valid subarrays count** = distance to next smaller element
4. This solution avoids the O(n²) brute force approach

---

## ✅ Solution Files

- **Problem Link**: [GeeksforGeeks](https://www.geeksforgeeks.org/problems/subarrays-with-first-element-minimum/1)
- **Solution Code**: [Solution.cpp](./solution.cpp) / [Solution.java](./solution.java) / [Solution.py](./solution.py)
- **Explanation**: This file (`explain.md`)

---

> **Note**: This solution runs in **O(n) time** and **O(n) space**, meeting all constraints for the problem.
