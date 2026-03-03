/////// solving using dqueue for efficient pops from the front
class Solution:
     def rearrangeQueue(self, q):
        r = deque()
        half = len(q) // 2
        for _ in range(half):
            r.append(q.popleft())
        for _ in range(half):
            q.append(r.popleft())
            q.append(q.popleft())