# 🪟 Longest Subarray with At Most Two Distinct Integers — 3 Approaches (Brute → Better → Optimal)

**Difficulty:** Medium

## 🧠 Problem Intuition

We need to find the **longest contiguous subarray** that contains **at most 2 distinct integers**.

### Key Insight:
The constraint is **local** - it depends on the **elements within the subarray**, not their positions.

When we add a new element:
- If total distinct ≤ 2: Valid, we can extend
- If total distinct > 2: Invalid, we must remove from the left

This suggests a **sliding window** approach.

---

## ✅ Approach 1 — Brute Force (Check every subarray)

### Intuition

For every possible subarray `[i, j]`:
1. **Count distinct integers** in that subarray
2. **If ≤ 2 distinct**: This is a valid subarray, track its length
3. **Find maximum** length among all valid subarrays

### Why it works

This is the **definitions-based approach** - we check every single subarray.

But we recalculate distinct count for each subarray → O(n²) or O(n³)

### Complexity

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n³) or O(n² · k) where k is distinct count check |
| **Space Complexity** | O(k) for hash set to track distinct elements |

### Code — Brute Force

```python
class Solution:
    def totalElements(self, arr):
        n = len(arr)
        max_length = 0
        
        # Try all possible subarrays [i, j]
        for i in range(n):
            distinct_set = set()
            
            for j in range(i, n):
                # Add element to the set
                distinct_set.add(arr[j])
                
                # If we have at most 2 distinct elements
                if len(distinct_set) <= 2:
                    max_length = max(max_length, j - i + 1)
                else:
                    # More than 2 distinct, no point extending further from i
                    break  # Optimization: stop extending from this i
        
        return max_length
```

### Step-by-Step Example

For array `[1, 2, 1, 2, 3]`:

```
i=0: j=0 → [1], distinct=1 ✓, length=1
     j=1 → [1,2], distinct=2 ✓, length=2
     j=2 → [1,2,1], distinct=2 ✓, length=3
     j=3 → [1,2,1,2], distinct=2 ✓, length=4
     j=4 → [1,2,1,2,3], distinct=3 ✗, break

i=1: j=1 → [2], distinct=1 ✓, length=1
     j=2 → [2,1], distinct=2 ✓, length=2
     j=3 → [2,1,2], distinct=2 ✓, length=3
     j=4 → [2,1,2,3], distinct=3 ✗, break

... (continuing for all i)

Maximum = 4
```

### Advantages & Disadvantages

✅ **Advantages**:
- Easy to understand - directly implements the problem definition
- No complex data structures needed

❌ **Disadvantages**:
- Very slow: O(n³) or O(n²)
- Inefficient for large arrays (n > 1000)
- Not suitable for interviews or production

---

## ✅ Approach 2 — Better (Basic Sliding Window)

### Intuition

Instead of checking all subarrays, use **two pointers** to maintain a valid window:

1. **Expand window** by moving right pointer
2. **Track frequencies** with a hash map
3. **Shrink window** from left when constraint is violated
4. **Record maximum** length

This avoids rechecking the same subarrays.

### Why it works

**Sliding Window Property**:
- If a window `[i, j]` is valid (≤ 2 distinct), and we shrink from left to get `[i+1, j]`, it's still valid or might become more valid.
- We never need to "restart" - pointers only move forward.

### Complexity

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) - at most 2-3 elements in map |

### Code — Basic Sliding Window

```python
class Solution:
    def totalElements(self, arr):
        from collections import defaultdict
        
        low = 0
        high = 0
        mp = defaultdict(int)
        ans = 0
        
        while high < len(arr):
            # Add element at high
            mp[arr[high]] += 1
            
            # Shrink if more than 2 distinct
            while len(mp) > 2:
                mp[arr[low]] -= 1
                if mp[arr[low]] == 0:
                    del mp[arr[low]]
                low += 1
            
            # Update max
            ans = max(ans, high - low + 1)
            high += 1
        
        return ans
```

### Step-by-Step Example

For array `[1, 2, 1, 2, 3]`:

```
high=0: Add 1 → mp={1:1}, valid, length=1, ans=1
high=1: Add 2 → mp={1:1, 2:1}, valid, length=2, ans=2
high=2: Add 1 → mp={1:2, 2:1}, valid, length=3, ans=3
high=3: Add 2 → mp={1:2, 2:2}, valid, length=4, ans=4
high=4: Add 3 → mp={1:2, 2:2, 3:1}, invalid (3 distinct)!
        
        Shrink:
        - Remove arr[0]=1 → mp={1:1, 2:2, 3:1}, still 3 distinct
        - low=0→1
        - Remove arr[1]=2 → mp={1:1, 2:1, 3:1}, still 3 distinct
        - low=1→2
        - Remove arr[2]=1 → mp={2:1, 3:1}, valid!
        - low=2→3
        
        length=4-3+1=2, ans=max(4,2)=4

ANSWER: 4
```

### Why It's Better

- ✅ O(n) time - each element visited at most twice
- ✅ O(1) space - at most 2-3 elements
- ✅ Single pass through array
- ✅ Much faster than brute force

### Disadvantages

- ❌ Requires understanding sliding window concept
- ❌ Off-by-one errors possible in pointer management

---

## ✅ Approach 3 — Optimal (Refined Sliding Window)

### Intuition

Same as Approach 2, but with **refined variable names** and **explicit documentation**:

- Use `low` and `high` (instead of `i` and `j`) for clarity
- More explicit pointer management
- Better structured with comments

### Why it's "Optimal"

Same time/space complexity as Approach 2: O(n) time, O(1) space.

The "optimization" is in **clarity and maintainability**, not raw performance.

### Complexity

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n) - each element at most twice |
| **Space Complexity** | O(1) - constant map size (≤ 3) |

### Code — Optimal Sliding Window

```python
class Solution:
    def totalElements(self, arr):
        from collections import defaultdict
        
        low = 0                             # Left boundary
        high = 0                            # Right boundary
        mp = defaultdict(int)               # Frequency map
        ans = 0                             # Maximum length
        
        while high < len(arr):
            # Step 1: Expand - Add current element
            mp[arr[high]] += 1
            
            # Step 2: Shrink - Constraint violation check
            while len(mp) > 2:
                mp[arr[low]] -= 1
                if mp[arr[low]] == 0:
                    del mp[arr[low]]
                low += 1
            
            # Step 3: Track - Update maximum
            ans = max(ans, high - low + 1)
            
            # Step 4: Continue - Move high
            high += 1
        
        return ans
```

### Why This Works

1. **Expand Phase**: Add `arr[high]` to window
2. **Validate Phase**: If distinct > 2, shrink from left
3. **Track Phase**: Record max valid window size
4. **Proceed Phase**: Move right pointer for next iteration

### The Beauty of Sliding Window

**Why O(n) and not O(n²)?**
- `low` pointer starts at 0 and ends at n-1 (moves right n times)
- `high` pointer starts at 0 and ends at n-1 (moves right n times)
- Total operations: 2n = O(n)
- Each element is processed at most twice

---

## 🎯 Summary Table

| Approach | Time | Space | Method | Best For |
|----------|------|-------|--------|----------|
| **1. Brute Force** | O(n³) or O(n²) | O(k) | Check every subarray | Understanding problem |
| **2. Basic Sliding Window** | O(n) | O(1) | Two pointers + map | Interviews |
| **3. Optimal Sliding Window** | O(n) | O(1) | Two pointers + documented | Production code |

---

## 🧠 Final Takeaway

### All approaches use the same principle:

**A subarray is valid if and only if it has at most 2 distinct integers.**

### The progression:

1. **Brute Force**: Verify this principle for every subarray → O(n³)
2. **Sliding Window**: Maintain the invariant efficiently → O(n)
3. **Optimal**: Polish and document the sliding window → O(n) with clarity

### Key Insight: The Sliding Window Invariant

At any point:
- Window `[low, high]` is **valid**: has ≤ 2 distinct elements
- We **never backtrack** `low` pointer (it only moves right)
- This guarantees O(n) because:
  - Total rightward movement of `low`: n steps
  - Total rightward movement of `high`: n steps
  - Combined: 2n = O(n)

### When to use each approach:

- **Brute Force**: Learning, understanding the problem
- **Sliding Window**: 99% of cases (interviews, LeetCode, production)
- **Optimized Sliding Window**: Production code with documentation

### Generalizable to "At Most K Distinct"

Simply change:
```python
while len(mp) > 2:  # Change to > k
```

Everything else stays the same! The solution scales beautifully.

### Why Sliding Window is Elegant

1. ✅ Solves the problem in **minimum time** O(n)
2. ✅ Uses **minimal space** O(1)
3. ✅ **Single pass** through array
4. ✅ No preprocessing needed
5. ✅ **Intuitive** once you understand the invariant
6. ✅ **Generalizable** to similar problems

**Remember:** The sliding window technique is one of the most powerful tools in algorithm design. Master it! 🎯
