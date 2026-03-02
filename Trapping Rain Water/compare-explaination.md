# 🌧️ Trapping Rain Water — 3 Approaches (Brute → Better → Optimal)

**Difficulty:** Hard

## 🧠 Problem Intuition

A bar at index `i` can trap water **ONLY if:**
- There is a taller/equal bar on the **left**
- There is a taller/equal bar on the **right**

The water trapped at index `i` is:

$$\text{water}[i] = \min(\text{leftMax}[i], \text{rightMax}[i]) - \text{height}[i]$$

**This is the entire problem.**

---

## ✅ Approach 1 — Brute Force (Check left & right max for each index)

### Intuition

For every bar `i`, manually scan:
- All bars to the **left** → find `leftMax`
- All bars to the **right** → find `rightMax`
- Then compute stored water at `i`

### Why it works

This is the **literal definition** of rainwater trapping.

But scanning left and right every time gives **O(n²) time** — very inefficient.

### Complexity

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n²) |
| **Space Complexity** | O(1) |

### Code — Brute Force

```cpp
class Solution {
  public:
    int maxWater(vector<int> &arr) {
        int n = arr.size();
        int ans = 0;

        // For each bar, check water it can trap
        for (int i = 1; i < n - 1; i++) {
            int lmax = 0, rmax = 0;

            // Find tallest bar to the left
            for (int j = i - 1; j >= 0; j--)
                lmax = max(lmax, arr[j]);

            // Find tallest bar to the right
            for (int j = i + 1; j < n; j++)
                rmax = max(rmax, arr[j]);

            // Water trapped = min of boundaries - current height
            int height = min(lmax, rmax);

            if (height > arr[i])
                ans += height - arr[i];
        }
        return ans;
    }
};
```

### Step-by-Step Example

For array `[3, 0, 1, 0, 4, 0, 2]`:

```
i=1 (height=0): lmax=3, rmax=4, min(3,4)=3, water=3-0=3
i=2 (height=1): lmax=3, rmax=4, min(3,4)=3, water=3-1=2
i=3 (height=0): lmax=3, rmax=4, min(3,4)=3, water=3-0=3
i=4 (height=4): lmax=3, rmax=2, min(3,2)=2, water=0 (2 < 4)
i=5 (height=0): lmax=4, rmax=2, min(4,2)=2, water=2-0=2

Total = 3 + 2 + 3 + 0 + 2 = 10 ✓
```

---

## ✅ Approach 2 — Precompute LeftMax & RightMax (DP Arrays)

### Intuition

Instead of scanning left & right for every index, we **prepare**:
- `leftMax[i]` = highest bar to the left (including i)
- `rightMax[i]` = highest bar to the right (including i)

We compute these arrays in **two passes**:
1. Left → Right: build `leftMax`
2. Right → Left: build `rightMax`

Now for each index: `water = min(leftMax, rightMax) - height`

### Why it works

We **reuse information**; no repeated scanning.

Each element is processed only **constant times**.

### Complexity

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n) |
| **Space Complexity** | O(n) |

### Code — LeftMax & RightMax Arrays

```cpp
class Solution {
  public:
    int maxWater(vector<int> &arr) {
        int n = arr.size();
        vector<int> left(n), right(n);

        // Build leftMax array: left[i] = max(arr[0..i])
        left[0] = arr[0];
        for (int i = 1; i < n; i++)
            left[i] = max(left[i - 1], arr[i]);

        // Build rightMax array: right[i] = max(arr[i..n-1])
        right[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--)
            right[i] = max(right[i + 1], arr[i]);

        // Compute trapped water for each position
        int ans = 0;
        for (int i = 0; i < n; i++)
            ans += max(0, min(left[i], right[i]) - arr[i]);

        return ans;
    }
};
```

### Step-by-Step Example

For array `[3, 0, 1, 0, 4, 0, 2]`:

```
Step 1: Build left array
left[0] = 3
left[1] = max(3, 0) = 3
left[2] = max(3, 1) = 3
left[3] = max(3, 0) = 3
left[4] = max(3, 4) = 4
left[5] = max(4, 0) = 4
left[6] = max(4, 2) = 4
→ left = [3, 3, 3, 3, 4, 4, 4]

Step 2: Build right array
right[6] = 2
right[5] = max(0, 2) = 2
right[4] = max(4, 2) = 4
right[3] = max(0, 4) = 4
right[2] = max(1, 4) = 4
right[1] = max(0, 4) = 4
right[0] = max(3, 4) = 4
→ right = [4, 4, 4, 4, 4, 2, 2]

Step 3: Calculate water at each position
i=0: min(3,4)-3 = 0
i=1: min(3,4)-0 = 3 ✓
i=2: min(3,4)-1 = 2 ✓
i=3: min(3,4)-0 = 3 ✓
i=4: min(4,4)-4 = 0
i=5: min(4,2)-0 = 2 ✓
i=6: min(4,2)-2 = 0

Total = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 ✓
```

---

## ✅ Approach 3 — Optimal Two-Pointer (O(1) Space)

### Core Intuition (VERY IMPORTANT ⭐)

At any moment, we have two pointers `l` and `r` moving towards each other.

**The key insight:**

If `leftMax <= rightMax`:
- → The **left side** determines the water level
- → We can safely process position `l` and move `l++`

If `rightMax < leftMax`:
- → The **right side** determines the water level
- → We can safely process position `r` and move `r--`

### Why this works

**Water trapped depends on the SHORTER boundary** (bottleneck principle).

Whichever side is shorter forms the **bottleneck** and can be processed immediately.

This logic **avoids extra arrays** and gives **optimal O(1) space** performance.

### Complexity

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) |

### Code — Two Pointer (Optimal)

```cpp
class Solution {
  public:
    int maxWater(vector<int> &arr) {
        int n = arr.size();
        int l = 0, r = n - 1;                    // Two pointers from ends
        int left_max = 0, right_max = 0;         // Max heights from each side
        int ans = 0;

        while (l < r) {
            // Left boundary is smaller or equal → process left
            if (arr[l] <= arr[r]) {
                // If current element is taller, update left_max
                if (arr[l] >= left_max) {
                    left_max = arr[l];
                } 
                // Otherwise, water trapped = left_max - current
                else {
                    ans += left_max - arr[l];
                }
                l++;
            }
            // Right boundary is smaller → process right
            else {
                // If current element is taller, update right_max
                if (arr[r] >= right_max) {
                    right_max = arr[r];
                } 
                // Otherwise, water trapped = right_max - current
                else {
                    ans += right_max - arr[r];
                }
                r--;
            }
        }

        return ans;
    }
};
```

### Step-by-Step Example

For array `[3, 0, 1, 0, 4, 0, 2]`:

```
Initial:  l=0(3), r=6(2), left_max=0, right_max=0, ans=0

Step 1: arr[0]=3 <= arr[6]=2? NO → Process right
        arr[6]=2 >= right_max=0? YES → right_max=2
        r=5

Step 2: arr[0]=3 <= arr[5]=0? NO → Process right
        arr[5]=0 >= right_max=2? NO → ans += 2-0=2
        r=4

Step 3: arr[0]=3 <= arr[4]=4? YES → Process left
        arr[0]=3 >= left_max=0? YES → left_max=3
        l=1

Step 4: arr[1]=0 <= arr[4]=4? YES → Process left
        arr[1]=0 >= left_max=3? NO → ans += 3-0=3, total=5
        l=2

Step 5: arr[2]=1 <= arr[4]=4? YES → Process left
        arr[2]=1 >= left_max=3? NO → ans += 3-1=2, total=7
        l=3

Step 6: arr[3]=0 <= arr[4]=4? YES → Process left
        arr[3]=0 >= left_max=3? NO → ans += 3-0=3, total=10
        l=4

Step 7: l=4, r=4, l < r? NO → Exit loop

Final answer = 10 ✓
```

---

## 🎯 Summary Table

| Approach | Time | Space | Intuition | Best For |
|----------|------|-------|-----------|----------|
| **1. Brute Force** | O(n²) | O(1) | For each bar, scan left & right | Understanding the problem |
| **2. DP Arrays** | O(n) | O(n) | Precompute left & right boundaries | Interviews, learning |
| **3. Two Pointer** | O(n) | O(1) | Use the smaller boundary to trap water | Production code, optimal |

---

## 🧠 Final Takeaway

### The Unified Formula

All three approaches apply the **same fundamental formula:**

$$\text{Water}[i] = \min(\text{maxLeft}[i], \text{maxRight}[i]) - \text{height}[i]$$

**They differ ONLY in how efficiently they compute the left and right boundaries:**

1. **Brute Force**: Recomputes boundaries every time → O(n²)
2. **DP Arrays**: Precomputes once → O(n) time, O(n) space
3. **Two Pointer**: Smartly processes from smaller boundary → O(n) time, O(1) space

### Key Insight: The Bottleneck Principle

Water level at any position is determined by the **MINIMUM** of the maximum heights on both sides.

The shorter boundary acts as a **bottleneck** and limits how much water can be trapped.

### Approach 3 is Optimal ⭐

**Approach 3 (Two-Pointer)** is the most elegant and efficient:
- ✅ Achieves **optimal O(n) time**
- ✅ Uses **minimal O(1) space**
- ✅ Clean and elegant logic
- ✅ Demonstrates deep understanding of the problem
- ✅ Preferred in production code and interviews

**Remember:** Master the intuition, and the code follows naturally! 🎯
