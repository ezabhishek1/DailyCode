class Solution:
    def largestSwap(self, s: str) -> str:
        # Convert string to list because strings are immutable in Python
        chars = list(s)
        
        # 1. Store the last occurrence of each digit (0-9)
        last = {digit: i for i, digit in enumerate(s)}
        
        # 2. Traverse the string from left to right
        for i, char in enumerate(chars):
            # 3. Look for a larger digit (from 9 down to current+1)
            for digit in "9876543210":
                if digit > char: # If a larger digit exists
                    # 4. Check if that larger digit appears after current index i
                    if last.get(digit, -1) > i:
                        # Perform the swap
                        target_idx = last[digit]
                        chars[i], chars[target_idx] = chars[target_idx], chars[i]
                        
                        # Return immediately after the first successful swap
                        return "".join(chars)
        
        # If no swap improved the string, return original
        return s