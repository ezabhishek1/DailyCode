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

## Code Explanation

### Python Version - Detailed Breakdown

```python
def minWindow(self, s, p):
    n1 = len(s)
    n2 = len(p)
    
    # Edge case: if pattern longer than string, impossible
    if n1 < n2:
        return ""
    
    # Initialize pointers
    left = 0
    right = 0
    res = ""
    mini = math.inf
    
    # Counter for required characters
    d2 = Counter(p)  # e.g., for p="ABC": {A:1, B:1, C:1}
    
    # 'have' tracks how many characters we've found
    have = 0
    
    # Expand window by moving right pointer
    while (right < n1):
        ch = s[right]
        
        # If current character is in pattern
        if ch in d2:
            # Decrement needed count (we found one instance)
            d2[ch] -= 1
            
            # Only count if this was actually needed (>= 0 after decrement)
            if d2[ch] >= 0:
                have += 1  # Increment matched characters count
    
        # Try to shrink window from left when we have all chars
        while (have == n2 and left < n1):
            # Check if current window is smaller than previous best
            if mini > (right - left + 1):
                mini = (right - left + 1)
                res = s[left:right+1]  # Store the window
            
            # Try removing leftmost character
            if s[left] in d2:
                # Increment back (we're removing this character)
                d2[s[left]] += 1
                
                # If count becomes positive, we lost a needed character
                if d2[s[left]] > 0:
                    have -= 1
            
            # Shrink window from left
            left += 1
        
        # Expand window from right
        right += 1
    
    return res
```

#### Line-by-Line Explanation:

1. **Length checks:** `n1 = len(s), n2 = len(p)`
   - Get lengths to avoid repeated function calls

2. **Early exit:** `if n1 < n2: return ""`
   - Pattern longer than string = impossible solution

3. **`d2 = Counter(p)`**
   - Creates frequency map of required characters
   - Example: p="ABC" → d2 = {A:1, B:1, C:1}

4. **`have` variable:**
   - Counts total matched characters from pattern
   - When `have == n2`, we have all required characters

5. **Main loop:** `while (right < n1):`
   - Expands window by moving right pointer through string

6. **Character matching:**
   ```python
   if ch in d2:
       d2[ch] -= 1
       if d2[ch] >= 0:
           have += 1
   ```
   - Only process if character is in pattern
   - Decrement count in d2
   - Only increment `have` if we actually needed more of this character

7. **Shrinking phase:** `while (have == n2 and left < n1):`
   - Runs when window is valid (has all characters)
   - Updates result if current window is smaller

8. **Removing from window:**
   ```python
   if d2[s[left]] > 0:
       have -= 1
   ```
   - Only decrement `have` if we're removing a character we needed

---

### C++ Version - Detailed Breakdown

```cpp
class Solution {
  public:
    // Helper function to check if current window is valid
    bool check(unordered_map<int,int>&ms, unordered_map<int,int>&mp) {
        // ms = current window character counts
        // mp = pattern character requirements
        
        // If window has fewer unique chars than needed, it's invalid
        if(ms.size() < mp.size())
            return false;
        
        // Check if all required characters have sufficient frequency
        for(auto it : mp) {
            // it.first = character, it.second = required count
            // If current window doesn't have enough of this char
            if(it.second > ms[it.first])
                return false;
        }
        return true;  // All characters satisfied
    }
    
    string minWindow(string &s, string &p) {
        // Create frequency map for pattern
        unordered_map<int,int> mp;
        for(auto it : p)
            mp[it]++;  // Count each character in pattern
        
        // Initialize tracking variables
        string ans = "";           // Result string
        int i = 0;                 // Left pointer
        int j = 0;                 // Right pointer
        unordered_map<int,int> ms; // Current window character counts
        
        // Sliding window logic
        while(i < s.size() && j < s.size()) {
            // Expand window: add character at j
            ms[s[j]]++;
            
            // Try to shrink window when valid
            while(check(ms, mp) && i < s.size()) {
                // Update answer if current window is smaller
                if(ans == "" || ans.size() > j - i + 1)
                    ans = s.substr(i, j - i + 1);
                
                // Shrink window from left
                ms[s[i]]--;
                if(ms[s[i]] == 0)
                    ms.erase(s[i]);  // Remove if count becomes 0
                i++;
            }
            
            // Expand window for next iteration
            j++;
        }
        
        return ans;
    }
};
```

#### Line-by-Line Explanation:

1. **`check()` function:** Validates if window contains all required characters
   ```cpp
   bool check(unordered_map<int,int>&ms, unordered_map<int,int>&mp)
   ```
   - `ms` = current window character frequencies
   - `mp` = pattern character requirements

2. **Size check:** `if(ms.size() < mp.size())`
   - If window has fewer unique characters than needed, it's invalid

3. **Frequency validation:**
   ```cpp
   for(auto it : mp) {
       if(it.second > ms[it.first])
           return false;
   }
   ```
   - Iterate through all required characters
   - If any character doesn't have enough count in window, return false
   - Otherwise, all characters satisfied

4. **Pattern mapping:** 
   ```cpp
   unordered_map<int,int> mp;
   for(auto it : p)
       mp[it]++;
   ```
   - Creates frequency map of pattern characters
   - Example: p="ABC" → mp = {A:1, B:1, C:1}

5. **Two pointers:** `i` (left) and `j` (right)
   - `i` = left boundary of window
   - `j` = right boundary of window
   - Both start at 0

6. **Outer loop:** `while(i < s.size() && j < s.size())`
   - Continues until both pointers reach end
   - Expands window by incrementing `j`

7. **Window expansion:** `ms[s[j]]++`
   - Add character at position `j` to current window
   - Increment its frequency count

8. **Inner loop:** `while(check(ms, mp) && i < s.size())`
   - Runs only when window is valid
   - Tries to minimize window size

9. **Update result:**
   ```cpp
   if(ans == "" || ans.size() > j - i + 1)
       ans = s.substr(i, j - i + 1);
   ```
   - Store window if it's first result or smaller than previous

10. **Window shrinking:**
    ```cpp
    ms[s[i]]--;
    if(ms[s[i]] == 0)
        ms.erase(s[i]);
    ```
    - Decrease count of leftmost character
    - Remove from map if count becomes 0 (cleanup)
    - Increment left pointer

---

## Key Differences Between Python and C++

| Aspect | Python | C++ |
|--------|--------|-----|
| **Frequency Check** | Decrement counter while expanding | Call `check()` function |
| **Matched Count** | Track with `have` variable | Re-check entire `mp` in function |
| **Efficiency** | O(1) check with `have` counter | O(k) where k = unique chars in p |
| **Edge Cases** | Explicit check for `n1 < n2` | Handled in loop conditions |
| **String Slicing** | `s[left:right+1]` | `s.substr(i, j-i+1)` |

**Overall:** Python approach is more efficient with O(n) actual time, while C++ checks validity each iteration making it slower, but both achieve correct results.

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
