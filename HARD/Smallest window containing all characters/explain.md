# Smallest Window Containing All Characters

## Problem Statement
Given two strings `s` and `p`, find the smallest contiguous substring of `s` that contains all the characters in `p`. If no such window exists, return an empty string.

**Example:**
- Input: s = "ADOBECODEBANC", p = "ABC"
- Output: "BANC" (smallest window is "BANC" containing all characters A, B, C)

---

## Approach: Sliding Window with Hashmap

### Intuition
Use a **two-pointer sliding window** technique:
1. Expand the window by moving the right pointer until all characters from `p` are included
2. Once we have a valid window, try to shrink it from the left to find the minimum length
3. Keep track of the minimum window found so far

### Algorithm

**Step 1:** Create a frequency map for characters in `p`
- Store how many times each character appears in `p`

**Step 2:** Use two pointers (left and right) on string `s`
- Expand window by moving right pointer
- Add characters to the current window map

**Step 3:** Check if current window is valid
- A window is valid when it contains all characters from `p` with required frequencies

**Step 4:** Shrink window from left
- Once valid, try to minimize the window size
- Move left pointer and update the minimum window

**Step 5:** Continue until right pointer reaches end

### Step-by-step Example
```
s = "ADOBECODEBANC"
p = "ABC"

Initial: need {A:1, B:1, C:1}

Step 1: Expand right to "ADOBEC"
  - Missing characters: need to continue
  
Step 2: Continue expanding until "ADOBECODEBAN"
  - Now we have all characters
  - Window: "ADOBECODEBAN" (length 11)

Step 3: Shrink from left
  - Remove 'A': "DOBECODEBA​NC" (still valid)
  - Remove 'D': "OBECODEBA​NC" (still valid)
  - Remove 'O': "BECODE​BANC" (still valid)
  - Remove 'B': "ECODEBANC" (still valid)
  - Continue until we can't shrink anymore
  
Final: "BANC" (length 4)
```

---

## Complexity Analysis

| Aspect | Complexity |
|--------|-----------|
| **Time** | O(n + m) where n = len(s), m = len(p) |
| **Space** | O(1) or O(26) since we store at most 26 letters |

**Explanation:**
- Each character in `s` is visited at most twice (once by right pointer, once by left pointer)
- Character frequency maps contain at most 26 English letters
- Despite nested loops, overall time is linear

---

## Code Explanation (Python Version)

```python
def minWindow(self, s, p):
    # Store character frequencies needed
    d2 = Counter(p)  # Required characters
    
    # Initialize variables
    left = right = 0
    have = 0  # Count of characters matched
    mini = float('inf')  # Minimum window length
    res = ""  # Result window
    
    # Expand window with right pointer
    while right < len(s):
        ch = s[right]
        
        # If character needed, decrement count
        if ch in d2:
            d2[ch] -= 1
            # If this character is still needed (count >= 0)
            if d2[ch] >= 0:
                have += 1  # One more character matched
        
        # Try to shrink window from left
        while have == len(p):  # Window is valid (all chars found)
            # Update minimum window
            if mini > (right - left + 1):
                mini = right - left + 1
                res = s[left:right+1]
            
            # Try removing leftmost character
            if s[left] in d2:
                d2[s[left]] += 1
                if d2[s[left]] > 0:
                    have -= 1  # Lost a matching character
            
            left += 1  # Shrink window
        
        right += 1  # Expand window
    
    return res
```

### Key Points:
1. **`have` counter:** Tracks how many characters from `p` we've found in current window
2. **`d2` modification:** We decrement when matching, increment when removing
3. **`d2[ch] >= 0` check:** Only count a character as "matched" when we actually need it
4. **Two-phase process:** Expand with right pointer, shrink with left pointer

---

## C++ Version Explanation

The C++ version uses a `check()` function to verify if current window contains all required characters:

```cpp
bool check(unordered_map<int,int>&ms, unordered_map<int,int>&mp) {
    if(ms.size() < mp.size()) return false;  // Not enough unique chars
    
    // Check if all chars have required frequency
    for(auto it : mp) {
        if(it.second > ms[it.first])
            return false;  // Not enough of this character
    }
    return true;
}
```

Then uses sliding window similarly to maintain minimum window.

---

## Key Insights

1. **Sliding Window Pattern:** This is a classic sliding window problem
2. **Character Frequency:** Tracking frequencies is crucial for validation
3. **Two Pointers:** Right expands, left shrinks - ensures linear time
4. **Early Termination:** Stop shrinking when window becomes invalid

---

## Related Problems
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Permutation in String
- Find All Anagrams in a String
