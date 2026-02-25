
#User function Template for python3

from collections import defaultdict
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        
        sm = 0
        
        res = 0
        
        dc = defaultdict(int)
        
        dc[0] = -1
        
        
        
        for ind, num in enumerate(arr):
            
            sm += 1 if num >k else -1
            
            
            if sm > 0:
                
                res = max(res, ind+1)
                
            else:
                if sm not in dc:
                    
                    dc[sm] = ind
                    
                if sm-1 in dc:
                    res = max(res, ind - dc[sm-1])
        return res


# ═══════════════════════════════════════════════════════════════
# APPROACH EXPLANATION: Prefix Sum with Removal Logic
# ═══════════════════════════════════════════════════════════════

"""
🔷 Core Concept: Prefix Sum Encoding

Step 1: Transform the array into prefix sums of encoded values
  - If arr[i] > k  → add +1
  - If arr[i] <= k → add -1

This creates a running sum that represents the "balance"
between elements greater than k vs less than/equal to k.

Step 2: Analyze the prefix sum

CASE 1: If sum > 0 at index i
  ✓ Subarray [0...i] has majority > k
  ✓ Check against answer: max(answer, i+1)
  
CASE 2: If sum <= 0 at index i
  ✗ Subarray [0...i] has majority <= k
  ✗ Need to remove a segment to balance it
  
  Key Insight:
  - Current balance is "sum" (which is ≤ 0)
  - If we previously had balance (sum-1), removing that segment leaves balance = 1 > 0
  - So if (sum-1) exists in our hashmap, we found a valid subarray!
  - Length = current_index - previous_index_of_(sum-1)

Step 3: Why the -1 check?

When sum <= 0:
  - We're in deficit (more elements ≤ k than > k)
  - To get sum > 0, we need to:
    * Either extend until sum naturally becomes positive
    * Or remove a segment that had sum = (sum-1)
  
  If we remove a segment with sum = (sum-1):
    - Remaining balance = (current_sum) - (removed_sum) = sum - (sum-1) = 1 > 0
    - That segment represents the minimum "bad" part we need to skip

Step 4: Example with Element Removal

arr = [5, 1, 3, 2, 4]
k = 2

Index  arr  >k?  Encoded  Prefix  Analysis
 -1         -           0       Initialize: dc[0] = -1
  0    5   YES   +1      1       sum > 0: res = max(0, 0+1) = 1
  1    1    NO   -1      0       sum = 0 = (1-1): appears at dc[0], res = 1-(-1) = 2
  2    3   YES   +1      1       sum > 0: res = max(2, 2+1) = 3
  3    2    NO   -1      0       sum = 0: already in dc, check dc[-1]? No
  4    4   YES   +1      1       sum > 0: res = max(3, 4+1) = 5

Answer: 5 (entire array has majority > 2)

🔷 Removal Principle

Number of elements to remove = abs(sum) + 1

Why?

If current sum = -3 (3 more elements ≤ k than > k)
We need to remove at least 1 element to shift balance:

If we remove a segment with net value -1:
  - Removes 1 element > k and 0 elements ≤ k, OR
  - Removes 0 elements > k and 1 element ≤ k
  
New balance = -3 - (-1) = -2 (still not positive)

We'd need to remove abs(-3)+1 = 4 elements worth of "bad" balance
to really get to positive territory.

Actually, the check (sum-1) in hashmap is the elegant way:
Instead of calculating removal size, we just ask:
"Have we seen balance (sum-1) before?"
If yes, the segment between was the problematic one to skip.

═══════════════════════════════════════════════════════════════
TIME & SPACE COMPLEXITY
═══════════════════════════════════════════════════════════════

Time Complexity: O(n)
  - Single pass through array
  - Each hashmap operation: O(1) average
  - Total: O(n)

Space Complexity: O(n)
  - Hashmap stores at most n unique prefix sums
  - Worst case: all prefix values are different
  - Total: O(n)

═══════════════════════════════════════════════════════════════
ALGORITHM FLOW
═══════════════════════════════════════════════════════════════

1. Initialize: 
   - sm = 0 (current prefix sum)
   - res = 0 (result)
   - dc = {0: -1} (stores first occurrence of each prefix sum)

2. For each element:
   - Add +1 if element > k, else add -1
   
   - If sm > 0:
     → Entire prefix [0...i] is valid
     → Update res = max(res, i+1)
   
   - Else (sm <= 0):
     → Check if we've seen (sm-1) before
     → If yes: valid subarray exists, length = i - dc[sm-1]
     → Update res with this length
   
   - Store current sum in hashmap if not already present

3. Return res

═══════════════════════════════════════════════════════════════
"""
        