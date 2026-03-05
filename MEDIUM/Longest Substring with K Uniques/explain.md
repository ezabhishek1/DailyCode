# Longest Substring with K Unique Characters

## Problem Statement
Given a string `s` and an integer `k`, find the length of the longest substring that contains exactly `k` distinct/unique characters. Return -1 if no such substring exists.

## Approach: Sliding Window with HashMap

### Intuition
Instead of checking all possible substrings (O(n²)), we use a sliding window technique:
- Maintain a window with exactly k distinct characters
- Expand the window by moving the right pointer
- When we have more than k distinct characters, shrink from the left
- Track the maximum length whenever we have exactly k distinct characters

### Algorithm
1. Initialize `char_count` (HashMap), `max_length = -1`, `start = 0`
2. For each position `end` from 0 to n-1:
   - Add `s[end]` to the window and increment its count
   - While we have more than k distinct characters:
     - Decrease count of `s[start]`
     - Remove character if count becomes 0
     - Move `start` forward
   - If we have exactly k distinct characters:
     - Update `max_length` with current window size: `end - start + 1`
3. Return `max_length`

### Complexity Analysis
- **Time Complexity**: O(n) - Each character is visited at most twice (once by right pointer, once by left)
- **Space Complexity**: O(k) - HashMap stores at most k distinct characters

---

## Detailed Walkthrough

### Example 1
```
s = "aabacbebebe", k = 3

Index: 0 1 2 3 4 5 6 7 8 9 10
Char:  a a b a c b e b e b e

Step-by-step:
end=0: char_count = {a:1}           → 1 distinct < 3
end=1: char_count = {a:2}           → 1 distinct < 3
end=2: char_count = {a:2, b:1}      → 2 distinct < 3
end=3: char_count = {a:3, b:1}      → 2 distinct < 3
end=4: char_count = {a:3, b:1, c:1} → 3 distinct = k ✓ len=5
end=5: char_count = {a:3, b:2, c:1} → 3 distinct = k ✓ len=6
end=6: char_count = {a:3, b:2, c:1, e:1} → 4 distinct > k
       Shrink: remove 'a' at start=0
       char_count = {a:2, b:2, c:1, e:1} → 4 distinct > k
       Shrink: remove 'a' at start=1
       char_count = {a:1, b:2, c:1, e:1} → 4 distinct > k
       Shrink: remove 'a' at start=2
       char_count = {b:2, c:1, e:1} → 3 distinct = k ✓ len=4
end=7: char_count = {b:3, c:1, e:1} → 3 distinct = k ✓ len=5
end=8: char_count = {b:3, c:1, e:2} → 3 distinct = k ✓ len=6
end=9: char_count = {b:4, c:1, e:2} → 3 distinct = k ✓ len=7
end=10: char_count = {b:4, c:1, e:3} → 3 distinct = k ✓ len=8

Maximum length with exactly 3 distinct characters = 8
Window: "cbebeebe" (indices 4-10, but adjusting for corrections: "cbebebe")
```

### Example 2
```
s = "aaaa", k = 2

end=0: char_count = {a:1}     → 1 distinct < 2
end=1: char_count = {a:2}     → 1 distinct < 2
end=2: char_count = {a:3}     → 1 distinct < 2
end=3: char_count = {a:4}     → 1 distinct < 2

Never reaches k=2, return -1
```

---

## Key Points

1. **Exactly k Characters**: Not "at most" or "at least" - must be exactly k
2. **HashMap for Frequency**: O(1) lookup and update of character counts
3. **Window Contraction**: Only shrink when we exceed k, never delete a valid window
4. **Early Termination**: Once we have >k characters, keep shrinking until we have exactly k
5. **Return -1**: If no substring with k distinct characters exists

---

## Edge Cases

1. **k > Total Distinct Characters**: Return -1
   ```
   s = "abc", k = 4 → return -1
   ```

2. **k = 1**: Find longest substring with single character
   ```
   s = "aabaab", k = 1 → return 3 (substring "aaa" doesn't exist, "aa" is length 2, "bb" is length 2)
   Actually: "aab" has 2 distinct, so max with k=1 is "aa" at start = 2
   ```

3. **Empty String**: s = "", k = anything → return -1

4. **k = 0**: Typically not valid input, but would return -1

---

## Approach 2: Last Occurrence (Optimized Shrinking)

### Intuition
Instead of storing frequencies, we can store only the **last occurrence index** of each character. When we exceed k distinct characters, we remove the character whose last occurrence is **earliest** (leftmost). This avoids the need to track exact frequencies and can be optimized.

### Algorithm
1. Initialize `last_occurrence` (HashMap), `max_length = -1`, `start = 0`
2. For each position `end` from 0 to n-1:
   - Update `last_occurrence[s[end]] = end`
   - While we have more than k distinct characters:
     - Find the character with the **minimum last occurrence** among characters in current window
     - Move `start` to that position + 1 (removes that character)
   - If we have exactly k distinct characters:
     - Update `max_length` with current window size
3. Return `max_length`

### Complexity Analysis
- **Time Complexity**: 
  - Naive: O(n × k) - for each violation, finding minimum takes O(k) with k distinct chars
  - Optimized: O(n × 26) = **O(n)** - only 26 English letters, so O(1) per minimum finding
- **Space Complexity**: O(k) = O(1) - At most k characters, bounded by 26

### Why This Works?

When we have more than k distinct characters, we want to remove one. The key insight is:
- Removing a character that hasn't appeared recently (small last occurrence) is safe
- It minimizes the chance of creating an invalid window
- We can safely move `start` to just after that character's position

### Example Comparison

```
s = "aabacbebebe", k = 3

Using Last Occurrence Approach:

end=4: last_occurrence = {a:3, b:1, c:4}
       Distinct = 3, window = "aabac" ✓

end=6: last_occurrence = {a:3, b:5, c:4, e:6}
       Distinct = 4 > 3
       Find min: min is 'a' at position 3
       Move start to 4 (remove 'a')
       Now: {b:5, c:4, e:6}, window = "bcbe"... checking validity

This approach avoids frequency tracking and directly targets the
character to be removed based on recency.
```

### Tradeoff Between Approaches

| Aspect | Frequency-based | Last Occurrence |
|--------|-----------------|-----------------|
| Implementation | Simpler | Slightly more complex |
| Time Complexity | O(n) | O(n × k) → O(n) with optimization |
| Space | O(k) | O(k) |
| Window Shrinking | Gradual (one char at a time) | Can be aggressive (jump to min) |
| Use Case | Interview-friendly | Optimized for large k |

**Recommendation**: Use **Approach 1 (Frequency-based)** for clarity in interviews. Use **Approach 2** when you need to optimize or demonstrate advanced thinking.

---

## Related Problems

- **Longest Substring Without Repeating Characters** - k = number of distinct chars
- **Longest Substring with At Most K Distinct** - Similar approach but condition is <= k
- **Subarrays with K Different Integers** - Array version of this problem
