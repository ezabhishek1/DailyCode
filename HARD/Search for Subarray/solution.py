class Solution:
    def search(self, a, b):
        n = len(a)
        m = len(b)

        # Build LPS array
        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and b[i] != b[j]:
                j = lps[j - 1]

            if b[i] == b[j]:
                j += 1
                lps[i] = j

        # KMP Search
        result = []
        i = j = 0

        while i < n:
            if a[i] == b[j]:
                i += 1
                j += 1

                if j == m:
                    result.append(i - m)
                    j = lps[j - 1]

            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return result