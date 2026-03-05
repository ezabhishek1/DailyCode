class Solution:
    def longestKSubstr(self, s, k):
        """
        Find the length of longest substring with exactly k unique characters.
        
        Args:
            s: Input string
            k: Number of unique characters to look for
            
        Returns:
            Length of longest substring with exactly k unique characters, or -1 if not found
        """
        n = len(s)
        max_len = -1        # Initialize to -1 (no valid substring found yet)
        char_count = {}     # Dictionary to store character frequencies
        start = 0           # Left pointer of sliding window

        # Expand window with right pointer
        for end in range(n):
            # Add current character and increment its count
            char_count[s[end]] = char_count.get(s[end], 0) + 1

            # Shrink window from left while we have more than k distinct characters
            while len(char_count) > k:
                # Decrease frequency of leftmost character
                char_count[s[start]] -= 1
                
                # Remove character from dictionary if frequency becomes 0
                if char_count[s[start]] == 0:
                    del char_count[s[start]]
                
                # Move left pointer to shrink window
                start += 1

            # Update max length when we have exactly k distinct characters
            if len(char_count) == k:
                # Current window size = end - start + 1
                max_len = max(max_len, end - start + 1)

        return max_len

