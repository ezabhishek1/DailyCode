import math

class Solution:
    def smallestDiff(self,a, b, c):
        a.sort()
        b.sort()
        c.sort()
        
        min_diff = math.inf
        tripet = [-1] * 3
        ptr1 = ptr2 = ptr3 = 0
        
        while ptr1 < len(a) and ptr2 < len(b) and ptr3 < len(c):
            maxx = max(a[ptr1], b[ptr2], c[ptr3])
            minn = min(a[ptr1], b[ptr2], c[ptr3])
            
            if min_diff > maxx - minn:
                triplet = [a[ptr1], b[ptr2], c[ptr3]]
                min_diff = maxx - minn
            
            if minn == a[ptr1]:
                ptr1 += 1
            elif minn == b[ptr2]:
                ptr2 += 1
            else:
                ptr3 += 1
            
        triplet.sort(reverse=True)
        return triplet