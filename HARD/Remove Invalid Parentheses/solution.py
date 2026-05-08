class Solution:
    def validParenthesis(self, s: str) -> list[str]:
        removals = self.computeMinRemovals(s)
        seen = set()
        results = []
        self.dfs(s, 0, removals, seen, results)
        return results
    def computeMinRemovals(self, s: str) -> int:
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left + right
    def isValid(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0

    def dfs(self, s: str, start: int, rem: int, seen: set, results: list):
        if rem == 0:
            if self.isValid(s) and s not in seen:
                seen.add(s)
                results.append(s)
            return
        n = len(s)
        for i in range(start, n):
            if s[i] != '(' and s[i] != ')':
                continue
            if i > start and s[i] == s[i - 1]:
                continue
            nxt = s[:i] + s[i+1:]
            self.dfs(nxt, i, rem - 1, seen, results)