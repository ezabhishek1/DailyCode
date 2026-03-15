class Solution:
    def generateIp(self, s):
        res = []

        def backtrack(start=0, path=[]):
            # If we've got 4 parts and used all digits, it's a valid IP
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try 1 to 3 digit segments
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start + length]
                # Skip if segment has leading zeros or value > 255
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(start + length, path + [segment])

        backtrack()
        return res

