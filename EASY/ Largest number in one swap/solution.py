class Solution:
    def largestSwap(self, s: str) -> str:
        chars = list(s)

        last = {digit: i for i, digit in enumerate(s)}
        
        for i, char in enumerate(chars):
            for digit in "9876543210":
                if digit > char: 
                    if last.get(digit, -1) > i:
                        target_idx = last[digit]
                        chars[i], chars[target_idx] = chars[target_idx], chars[i]
                        return "".join(chars)
        return s