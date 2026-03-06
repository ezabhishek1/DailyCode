import math
from collections import Counter

class Solution:
    def minWindow(self, s, p):
        """
        Find the smallest contiguous substring of s that contains all characters in p.
        Uses sliding window with two pointers approach.
        
        Time Complexity: O(n + m) where n = len(s), m = len(p)
        Space Complexity: O(1) - at most 26 lowercase letters
        """
        
        # Get lengths of both strings
        n1 = len(s)  # Length of main string
        n2 = len(p)  # Length of pattern string
        
        # Edge case: pattern longer than string is impossible
        if n1 < n2:
            return ""
        
        # Initialize two pointers for sliding window
        left = 0   # Left boundary of window
        right = 0  # Right boundary of window
        res = ""   # Store result window
        mini = math.inf  # Track minimum window size found
        
        # Counter for required characters from pattern
        # Maps each character to how many times we need it
        # Example: p="ABC" -> d2 = {A:1, B:1, C:1}
        d2 = Counter(p)
        
        # Track how many characters from pattern we've matched
        # When have == n2, we have all required characters
        have = 0
        
        # PHASE 1: EXPAND WINDOW
        # Move right pointer to expand window and add characters
        while (right < n1):
            # Get character at right pointer
            ch = s[right]
            
            # If this character is in our pattern, process it
            if ch in d2:
                # Decrement the required count (we found one instance)
                d2[ch] -= 1
                
                # Only increment 'have' if we actually needed more of this character
                # d2[ch] >= 0 means we haven't exceeded the requirement yet
                if d2[ch] >= 0:
                    have += 1  # We've matched one more character from pattern
            
            # PHASE 2: SHRINK WINDOW
            # Once we have all required characters, try to minimize window
            while (have == n2 and left < n1):
                # Check if current window is smaller than our previous best
                if mini > (right - left + 1):
                    mini = (right - left + 1)  # Update minimum size
                    res = s[left:right+1]      # Store the window substring
                
                # Try removing the leftmost character from window
                if s[left] in d2:
                    # We're removing this character, so increment its count
                    d2[s[left]] += 1
                    
                    # If count becomes positive (>0), we no longer have all chars
                    if d2[s[left]] > 0:
                        have -= 1  # We've lost a matched character
                
                # Move left pointer to shrink window
                left += 1
            
            # Move right pointer to expand window
            right += 1
        
        # Return the smallest window found, or empty string if none
        return res
