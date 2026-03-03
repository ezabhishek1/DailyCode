class Solution:
    def overlapInt(self, arr):
        events = []
        for s, e in arr:
            events.append((s, 1))
            events.append((e + 1, -1))  # use e+1 because intervals are inclusive

        events.sort()
        curr = 0
        best = 0
        i = 0
        n = len(events)
        while i < n:
            x = events[i][0]
            delta = 0
            while i < n and events[i][0] == x:
                delta += events[i][1]
                i += 1
            curr += delta
            if curr > best:
                best = curr
        return best
        