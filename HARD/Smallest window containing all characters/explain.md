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

### Java Version - Detailed Breakdown

```java
class Solution {
    public static String minWindow(String s, String p) {
        // Edge case: pattern longer than string
        if (s.length() < p.length()) return "";
        
        // Frequency map for required characters in pattern
        Map<Character, Integer> need = new HashMap<>();
        for (char c : p.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }
        
        // Map to track characters in current window
        Map<Character, Integer> window = new HashMap<>();
        
        // haveCount = number of matched character frequencies
        // needCount = total characters needed (length of p)
        int haveCount = 0, needCount = p.length();
        int left = 0, minLen = Integer.MAX_VALUE, start = 0;
        
        // Expand window by moving right pointer
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            
            // Add character to current window
            window.put(c, window.getOrDefault(c, 0) + 1);
            
            // Check if this character matches a required character
            if (need.containsKey(c) && window.get(c) <= need.get(c)) {
                haveCount++;
            }
            
            // Shrink window from left when we have all characters
            while (haveCount == needCount) {
                // Update result if current window is smaller
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    start = left;
                }
                
                // Remove leftmost character from window
                char leftChar = s.charAt(left);
                window.put(leftChar, window.get(leftChar) - 1);
                
                // Check if we're removing a required character
                if (need.containsKey(leftChar) && width.get(leftChar) < need.get(leftChar)) {
                    haveCount--;
                }
                left++;
            }
        }
        
        // Return minimum window or empty string if not found
        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}
```

#### Line-by-Line Explanation:

1. **Edge case handling:** `if (s.length() < p.length()) return ""`
   - If pattern is longer than string, no valid window exists

2. **Build need map:**
   ```java
   Map<Character, Integer> need = new HashMap<>();
   for (char c : p.toCharArray()) {
       need.put(c, need.getOrDefault(c, 0) + 1);
   }
   ```
   - Creates frequency map of required characters
   - `.getOrDefault()` returns 0 if key doesn't exist
   - Example: p="ABC" → need = {A:1, B:1, C:1}

3. **Initialize window map:**
   ```java
   Map<Character, Integer> window = new HashMap<>();
   ```
   - Tracks character frequencies in current sliding window

4. **Key variables:**
   - `haveCount`: Number of character instances we've matched
   - `needCount`: Total characters needed from pattern (p.length())
   - `left`: Left boundary of window (starts at 0)
   - `minLen`: Length of smallest valid window found
   - `start`: Starting index of smallest valid window

5. **Expand window loop:** `for (int right = 0; right < s.length(); right++)`
   - Iterates through string with right pointer
   - Adds each character to the current window

6. **Add to window:**
   ```java
   window.put(c, window.getOrDefault(c, 0) + 1);
   ```
   - Increment frequency of character in window
   - Uses `.getOrDefault()` to handle new characters

7. **Check character match:**
   ```java
   if (need.containsKey(c) && window.get(c) <= need.get(c)) {
       haveCount++;
   }
   ```
   - Only increment `haveCount` if:
     - Character is in pattern (`need.containsKey(c)`)
     - We haven't exceeded the needed count (`window.get(c) <= need.get(c)`)
   - This prevents counting extra occurrences

8. **Shrink phase:** `while (haveCount == needCount)`
   - Runs only when current window contains all required characters
   - Tries to minimize window size by removing characters from left

9. **Update result:**
   ```java
   if (right - left + 1 < minLen) {
       minLen = right - left + 1;
       start = left;
   }
   ```
   - If current window is smaller than previous minimum:
     - Update `minLen` with new window size
     - Save starting index in `start`
   - Window size = `right - left + 1` (inclusive)

10. **Remove from left:**
    ```java
    char leftChar = s.charAt(left);
    window.put(leftChar, window.get(leftChar) - 1);
    ```
    - Decrement frequency of leftmost character
    - Prepares to move left pointer

11. **Check if we lost a match:**
    ```java
    if (need.containsKey(leftChar) && window.get(leftChar) < need.get(leftChar)) {
        haveCount--;
    }
    ```
    - Only decrement `haveCount` if:
      - Character was in pattern
      - We now have fewer than needed (`window.get(leftChar) < need.get(leftChar)`)
    - This marks window as invalid for next iteration

12. **Move left pointer:** `left++`
    - Shrinks window from left side

13. **Return result:**
    ```java
    return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    ```
    - If `minLen` is still `Integer.MAX_VALUE`, no valid window found → return ""
    - Otherwise, return `s.substring(start, start + minLen)`
      - First param: starting index
      - Second param: ending index (exclusive, so we add minLen)

---

### Java vs Python vs C++ Comparison

| Aspect | Java | Python | C++ |
|--------|------|--------|-----|
| **Frequency Check** | Increment `haveCount` while expanding | Decrement counter while expanding | Call `check()` function |
| **Matched Count** | Track with `haveCount` variable | Track with `have` variable | Re-check entire `mp` |
| **Time Complexity** | O(n + m) | O(n + m) | O(n + m) amortized |
| **Space Complexity** | O(k) where k ≤ 26 | O(k) where k ≤ 26 | O(k) where k ≤ 26 |
| **String Operations** | `charAt()`, `substring()` | String slicing `[:]` | `substr()` |
| **Map Methods** | `.getOrDefault()`, `.containsKey()` | `in` operator, `Counter` | `.erase()` |
| **Efficiency** | Most efficient - direct counter | Efficient - counter tracking | Slightly slower - validation checks |

**Summary:** Java and Python versions use the same efficient counter-based approach, making them both O(n) in practice. C++ version is correct but less efficient due to repeated validity checks.

---

## Key Differences Between Approaches

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
