
# 📐 Pythagorean Triplet - Complete Explanation

## 📋 Problem Statement
Given an array of integers `arr[]`, determine if there exists a **Pythagorean triplet** `(a, b, c)` such that:
- `a² + b² = c²`
- `a`, `b`, and `c` are elements of the array
- The triplet can be in any order (a and b are the legs, c is the hypotenuse)

---

## 🧪 Examples

### Example 1: `arr = [3, 2, 4, 6, 5]`
**Output:** `true`

**Explanation:**
- The triplet `(3, 4, 5)` forms a Pythagorean triplet
- Check: 3² + 4² = 9 + 16 = 25 = 5² ✓
- All three numbers (3, 4, 5) are present in the array

**Verification of all possible combinations:**
| a | b | c | a² + b² | c² | Valid? |
|---|---|---|---------|----|--------|
| 3 | 4 | 5 | 9+16=25 | 25 | ✓ **YES** |
| 3 | 2 | 4 | 9+4=13 | 16 | ✗ |
| 3 | 6 | 5 | 9+36=45 | 25 | ✗ |
| 2 | 4 | 6 | 4+16=20 | 36 | ✗ |
| 4 | 6 | 5 | 16+36=52 | 25 | ✗ |

---

### Example 2: `arr = [3, 8, 5]`
**Output:** `false`

**Explanation:**
- Check all possible combinations:

| a | b | c | a² + b² | c² | Valid? |
|---|---|---|---------|----|--------|
| 3 | 8 | 5 | 9+64=73 | 25 | ✗ |
| 3 | 5 | 8 | 9+25=34 | 64 | ✗ |
| 8 | 5 | 3 | 64+25=89 | 9 | ✗ |

- No combination satisfies a² + b² = c²
- The common triplet (3,4,5) can't be formed because 4 is missing

---

### Example 3: `arr = [1, 1, 1]`
**Output:** `false`

**Explanation:**
- All elements are 1
- Check: 1² + 1² = 1 + 1 = 2
- 2 ≠ 1² (which is 1)
- No combination works because 1² + 1² would need c² = 2, but √2 is not an integer and not in array

---

## 🚀 Solution Approaches

### Approach 1: Brute Force (O(n³))
```python
def pythagoreanTriplet_bruteforce(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = arr[i], arr[j], arr[k]
                if a*a + b*b == c*c:
                    return True
                if a*a + c*c == b*b:
                    return True
                if b*b + c*c == a*a:
                    return True
    return False
```

### Approach 2: Using Set (O(n²))
```python
def pythagoreanTriplet_set(arr):
    n = len(arr)
    squares = {x*x for x in arr}
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]*arr[i] + arr[j]*arr[j] in squares:
                return True
    return False
```

### Approach 3: Using Set with Optimization (O(n²) but faster)
```python
def pythagoreanTriplet(arr):
    squares = {x*x for x in arr}
    
    # Convert to list of squares for iteration
    sq_list = list(squares)
    n = len(sq_list)
    
    for i in range(n):
        for j in range(i+1, n):
            if sq_list[i] + sq_list[j] in squares:
                return True
    return False
```

### Approach 4: Sorting + Two Pointers (O(n²))
```python
def pythagoreanTriplet_twoPointers(arr):
    # Square all elements
    squares = [x*x for x in arr]
    squares.sort()
    n = len(squares)
    
    # Fix c (largest)
    for k in range(n-1, 1, -1):
        left = 0
        right = k-1
        
        while left < right:
            if squares[left] + squares[right] == squares[k]:
                return True
            elif squares[left] + squares[right] < squares[k]:
                left += 1
            else:
                right -= 1
    return False
```

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Pros | Cons |
|----------|----------------|------------------|------|------|
| **Brute Force** | O(n³) | O(1) | Simple | Very slow for large n |
| **Set Method** | O(n²) | O(n) | Good balance | Still O(n²) |
| **Two Pointers** | O(n²) | O(1) | No extra space | Requires sorting |

---

## 🔍 Detailed Walkthrough for Example 1: `[3, 2, 4, 6, 5]`

### Using Set Approach:

**Step 1:** Create set of squares
```
arr = [3, 2, 4, 6, 5]
squares = {9, 4, 16, 36, 25}
```

**Step 2:** Check all pairs (i, j)

| i | arr[i] | a² | j | arr[j] | b² | a² + b² | In squares? |
|---|---:|---|--|---:|---:|---:|:---:|
| 0 | 3 | 9 | 1 | 2 | 4 | 13 | ✗ |
| 0 | 3 | 9 | 2 | 4 | 16 | **25** | ✓ **(Found!)** |
| 0 | 3 | 9 | 3 | 6 | 36 | 45 | ✗ |
| 0 | 3 | 9 | 4 | 5 | 25 | 34 | ✗ |
| 1 | 2 | 4 | 2 | 4 | 16 | 20 | ✗ |
| 1 | 2 | 4 | 3 | 6 | 36 | 40 | ✗ |
| 1 | 2 | 4 | 4 | 5 | 25 | 29 | ✗ |
| 2 | 4 | 16 | 3 | 6 | 36 | 52 | ✗ |
| 2 | 4 | 16 | 4 | 5 | 25 | 41 | ✗ |
| 3 | 6 | 36 | 4 | 5 | 25 | 61 | ✗ |

**Result:** Found 9 + 16 = 25 ✓ → Return `True`

---

## 🧪 Edge Cases

| Test Case | Input | Expected | Explanation |
|-----------|-------|----------|-------------|
| **Empty array** | `[]` | `false` | No elements to form triplet |
| **Single element** | `[5]` | `false` | Need at least 3 numbers |
| **Two elements** | `[3,4]` | `false` | Need at least 3 numbers |
| **Perfect triplet** | `[3,4,5]` | `true` | Classic 3-4-5 triplet |
| **Multiple of triplet** | `[6,8,10]` | `true` | 6-8-10 works (2×3-4-5) |
| **All same number** | `[1,1,1]` | `false` | 1²+1² ≠ 1² |
| **Large numbers** | `[5,12,13]` | `true` | 5-12-13 triplet |
| **Unsorted array** | `[10,6,8]` | `true` | 6-8-10 still works |
| **Missing middle** | `[3,5,4]` | `true` | Order doesn't matter |
| **No triplet** | `[2,3,4]` | `false` | 4+9=13 ≠ 16 |

---

## ✅ Complete Solution Code

```python
class Solution:
    def pythagoreanTriplet(self, arr):
        # Create a set of squares for O(1) lookup
        squares = {x*x for x in arr}
        
        # Convert to list for iteration
        nums = list(squares)
        n = len(nums)
        
        # Check all pairs
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] in squares:
                    return True
        
        return False


# Test cases
sol = Solution()
print(sol.pythagoreanTriplet([3, 2, 4, 6, 5]))  # True
print(sol.pythagoreanTriplet([3, 8, 5]))        # False
print(sol.pythagoreanTriplet([1, 1, 1]))        # False
```

---

## 🎯 Key Takeaways

1. **Pythagorean triplets** satisfy a² + b² = c²
2. The **order doesn't matter** - any of the three numbers can be c
3. A **set of squares** allows O(1) lookup for the sum
4. The solution must check **all pairs** of numbers as potential a and b
5. **Time complexity**: O(n²) which is acceptable for n ≤ 10⁴
6. **Space complexity**: O(n) for storing squares

---

## 📈 Optimization Tips

- **Use set for O(1) lookup** instead of list search
- **Sort first** if using two-pointer approach
- **Handle duplicates** carefully (like [1,1,1] returns false)
- **Early exit** as soon as a triplet is found

---

## ✅ Solution Files

- **Problem Link**: [GeeksforGeeks](https://www.geeksforgeeks.org/problems/pythagorean-triplet/0)
- **Solution Code**: [Solution.py](./solution.py)

> **Note**: This problem is a variation of finding Pythagorean triplets in an array and appears in many coding interviews!
