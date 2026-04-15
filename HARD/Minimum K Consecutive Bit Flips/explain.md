# Minimum K Consecutive Bit Flips

## Problem Statement

You are given a binary array `arr[]` of size `n` and an integer `k`.

A **K-bit flip** means choosing a subarray of length `k` and toggling every element in it (0 → 1, 1 → 0).

Return the **minimum number of K-bit flips** required to make every element of the array `1`.  
If it is **impossible**, return `-1`.

**Constraints:**
- `1 ≤ n ≤ 10^5`
- `1 ≤ k ≤ n`
- `arr[i]` is either `0` or `1`

---

## Examples

### Example 1
```
Input:  arr = [0, 1, 0], k = 1
Output: 2
Explanation: Flip arr[0] → [1,1,0], then flip arr[2] → [1,1,1]. Total = 2 flips.
```

### Example 2
```
Input:  arr = [1, 1, 0], k = 2
Output: -1
Explanation: Only arr[2] is 0 but a window of size 2 starting at index 2 exceeds bounds.
```

### Example 3
```
Input:  arr = [0, 0, 0, 1, 0, 1, 1, 0], k = 3
Output: 3
Explanation:
  Flip [0..2] → [1,1,1,1,0,1,1,0]
  Flip [4..6] → [1,1,1,1,1,0,0,0]
  Flip [5..7] → [1,1,1,1,1,1,1,1]
  Total = 3 flips.
```

---

## Approach 1: Brute Force (Simulation)

### Idea

Traverse the array from **left to right**.

- Whenever you see a `0` at position `i`, flip all elements in `arr[i..i+k-1]` manually.
- Count flips.
- If a flip would go **out of bounds** (`i + k > n`), return `-1`.
- Continue until the end.

### Dry Run (Example 3)

```
arr = [0,0,0,1,0,1,1,0], k=3

i=0: arr[0]=0 → flip [0..2] → [1,1,1,1,0,1,1,0], count=1
i=1: arr[1]=1 → skip
i=2: arr[2]=1 → skip
i=3: arr[3]=1 → skip
i=4: arr[4]=0 → flip [4..6] → [1,1,1,1,1,0,0,0], count=2
i=5: arr[5]=0 → flip [5..7] → [1,1,1,1,1,1,1,1], count=3
i=6: arr[6]=1 → skip
i=7: arr[7]=1 → skip
Answer = 3 ✅
```

### Code (C++)

```cpp
class Solution {
public:
    int kBitFlips(vector<int>& arr, int k) {
        int n = arr.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) {
                if (i + k > n) return -1;   // can't flip, out of bounds
                count++;
                // flip k bits starting at i
                for (int j = i; j < i + k; j++)
                    arr[j] ^= 1;
            }
        }
        return count;
    }
};
```

### Code (Python)

```python
class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        count = 0
        for i in range(n):
            if arr[i] == 0:
                if i + k > n:
                    return -1
                count += 1
                for j in range(i, i + k):
                    arr[j] ^= 1
        return count
```

### Complexity

| | |
|---|---|
| **Time** | O(n × k) — for each `0` we flip k elements |
| **Space** | O(1) — in-place modification |

---

## Approach 2: Optimized — Greedy + Sliding Window (Queue)

### Key Insight

We don't need to physically flip bits. Instead, we can **track how many flips have covered position `i`**:

- If the number of active flips covering `i` is **odd**, bit `i` is effectively toggled.
- If it is **even** (or zero), bit `i` is unchanged.

We maintain a **queue** that stores the **end index** of each flip window we've started.  
When `i` reaches the front of the queue, that flip's window has expired and is popped.

**Queue size = number of active flips covering index `i`.**

At each index `i`:
1. If `q.front() == i`, pop it (flip expired).
2. Compute the **effective bit** = `arr[i] XOR (queue.size() % 2)`.
3. If effective bit is `0` → we must flip here:
   - If `i + k > n` → impossible, return `-1`.
   - Else push `i + k` into queue and increment count.

### Dry Run (Example 3)

```
arr = [0,0,0,1,0,1,1,0], k=3, n=8
queue=[], count=0

i=0: queue empty. effective=arr[0]^0=0 → flip! push 3. queue=[3], count=1
i=1: front=3≠1. effective=arr[1]^(1%2)=0^1=1 → no flip
i=2: front=3≠2. effective=arr[2]^(1%2)=0^1=1 → no flip
i=3: front=3==3 → pop. queue=[]. effective=arr[3]^0=1 → no flip
i=4: queue empty. effective=arr[4]^0=0 → flip! push 7. queue=[7], count=2
i=5: front=7≠5. effective=arr[5]^1=1^1=0 → flip! push 8. queue=[7,8], count=3
i=6: front=7≠6. effective=arr[6]^(2%2)=1^0=1 → no flip
i=7: front=7==7 → pop. queue=[8]. effective=arr[7]^(1%2)=0^1=1 → no flip

Answer = 3 ✅
```

### Code (C++) — O(k) space

```cpp
class Solution {
public:
    int kBitFlips(vector<int>& arr, int k) {
        int n = arr.size();
        queue<int> q;
        int operation = 0;

        for (int i = 0; i < n; i++) {
            // Remove expired flip window
            if (!q.empty() && i == q.front()) q.pop();

            int bit = arr[i];
            // If odd number of active flips, bit is toggled
            if (!q.empty() && q.size() % 2 == 1) bit ^= 1;

            if (bit == 0) {              // still 0 → must flip
                if (i + k > n) return -1;
                operation++;
                q.push(i + k);           // mark when this flip expires
            }
        }
        return operation;
    }
};
```

### Code (Python) — O(n) space (difference array variant)

```python
class Solution:
    def kBitFlips(self, arr, k):
        lth = len(arr)
        status = [0] * (lth + 1)  # difference array to track flip toggles
        cur = cnt = 0

        for ix, ve in enumerate(arr):
            cur ^= status[ix]           # apply any flip that ends here
            if ve ^ cur == 0:           # effective bit is 0 → need to flip
                cur ^= 1
                if ix + k <= lth:
                    status[ix + k] ^= 1 # mark end of this flip window
                else:
                    return -1           # out of bounds
                cnt += 1
        return cnt
```

### Complexity

| | |
|---|---|
| **Time** | O(n) — single pass through the array |
| **Space** | O(k) for queue / O(n) for difference array |

---

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute Force | O(n × k) | O(1) | Simple to understand, slow for large inputs |
| Greedy + Queue | O(n) | O(k) | Optimal, uses sliding window intuition |
| Difference Array | O(n) | O(n) | Cleaner code, same time as queue approach |

---

## When to Use This Pattern

- Problems where you need to track **overlapping range updates** without physically applying them.
- Any problem that involves **toggling windows** or **range flips** — the difference array / XOR trick is very powerful.
- Similar problems: *Flip String to Monotone Increasing*, *Minimum Number of K Consecutive Bit Flips* (LeetCode 995).

---

## References

- 📹 Intuition (Sliding Window + Queue): https://youtu.be/Mxca8kfzWEk — Must Watch!
- 🔗 GFG Problem: https://www.geeksforgeeks.org/minimum-number-of-flips-to-make-all-1s/