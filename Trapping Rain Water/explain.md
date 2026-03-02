# Trapping Rain Water

**Difficulty:** Hard | **Accuracy:** 33.14% | **Submissions:** 501K+ | **Points:** 8 | **Average Time:** 20m

## Problem Statement

Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.

## Examples

### Example 1:
- **Input:** `arr[] = [3, 0, 1, 0, 4, 0, 2]`
- **Output:** `10`
- **Explanation:** Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

### Example 2:
- **Input:** `arr[] = [3, 0, 2, 0, 4]`
- **Output:** `7`
- **Explanation:** Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.

### Example 3:
- **Input:** `arr[] = [1, 2, 3, 4]`
- **Output:** `0`
- **Explanation:** We cannot trap water as there is no height bound on both sides.

### Example 4:
- **Input:** `arr[] = [2, 1, 5, 3, 1, 0, 4]`
- **Output:** `9`
- **Explanation:** Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.

## Constraints

- `1 < arr.size() < 10^5`
- `0 < arr[i] < 10^3`

## Core Concept

Water can be trapped at position `i` if there are taller or equal height blocks on both sides. The amount of water trapped at position `i` is:

$$\text{water\_at\_i} = \min(\text{max\_left}, \text{max\_right}) - \text{arr}[i]$$

where:
- `max_left` = maximum height to the left of position i (including i)
- `max_right` = maximum height to the right of position i (including i)
- `arr[i]` = height at position i

## Approaches

### Approach 1: Two-Pointer with Max Tracking (C++)

This approach uses two pointers from both ends, maintaining the maximum height encountered so far from each direction.

**Algorithm**:
1. Initialize two pointers: `left = 0`, `right = arr.size() - 1`
2. Initialize two max trackers: `left_max = 0`, `right_max = 0`
3. Move pointers towards each other:
   - If `arr[left] <= arr[right]`:
     - If `arr[left] >= left_max`, update `left_max`
     - Else, add `left_max - arr[left]` to water trapped
     - Increment `left`
   - Else:
     - If `arr[right] >= right_max`, update `right_max`
     - Else, add `right_max - arr[right]` to water trapped
     - Decrement `right`

**Why it works**: 
- We move the pointer from the side with smaller height
- The smaller height acts as the bottleneck for water level
- At any position, if we know the max from one side and the current height, the water level is determined by the smaller of the two max values

**Visualization**:
```
arr:    [3, 0, 1, 0, 4, 0, 2]
left:    L           R
         Process left side since arr[left]=3 <= arr[right]=2 is false
         Actually arr[left]=3 > arr[right]=2, so process right
         
Step by step: We process smaller sides first, tracking maximums from both ends
```

### Approach 2: Prefix-Suffix Maximum Arrays (Python)

This approach precomputes the maximum heights to the left and right of each position.

**Algorithm**:
1. **Precompute left maximum**: For each position i, store the maximum height seen from start to i
   - `left[i] = max(left[0..i])`
   
2. **Precompute right maximum**: For each position i, store the maximum height seen from i to end
   - `right[i] = max(right[i..n-1])`
   
3. **Calculate trapped water**: For each position i:
   - Water at i = `min(left[i], right[i]) - arr[i]`
   
4. **Sum all water**: Add water trapped at each position

**Why it works**:
- We have complete information about maximums on both sides before calculating water
- Simple and straightforward calculation
- Clear separation of concerns: precompute, then calculate

**Example trace for [3, 0, 1, 0, 4, 0, 2]**:
```
arr:   [3, 0, 1, 0, 4, 0, 2]
left:  [3, 3, 3, 3, 4, 4, 4]  (max from start to each position)
right: [4, 4, 4, 4, 4, 2, 2]  (max from each position to end)

Position 0: min(3, 4) - 3 = 0
Position 1: min(3, 4) - 0 = 3  ← 3 units trapped
Position 2: min(3, 4) - 1 = 2  ← 2 units trapped
Position 3: min(3, 4) - 0 = 3  ← 3 units trapped
Position 4: min(4, 4) - 4 = 0
Position 5: min(4, 2) - 0 = 2  ← 2 units trapped
Position 6: min(4, 2) - 2 = 0

Total: 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 ✓
```

### Approach 3: Suffix-Max Array with On-the-Fly Prefix-Max (Python)

This approach is a **space-optimized hybrid** that combines precomputation with on-the-fly calculations:

**Algorithm**:
1. **Precompute suffix maximum**: Build array storing maximum height from each position to the end (similar to Approach 2's right array)
   - Uses `accumulate()` with `reversed()` for elegant implementation
   - Space: O(n) for suffix_max array

2. **On-the-fly prefix maximum**: Maintain prefix_max while iterating
   - Updates prefix_max as we traverse the array
   - Eliminates need for separate prefix array
   - Space: O(1) for prefix_max variable

3. **Calculate water**: For each position i (from 1 to n-2):
   - Water at i = `min(prefix_max, suffix_max[i+1]) - arr[i]`
   - Note: Uses `suffix_max[i+1]` (next position's max) not `suffix_max[i]`
   - Updates prefix_max for next iteration

**Why it works**:
- **Hybrid optimization**: Trades space vs computation smartly
- Only one array precomputed, other calculated on-the-fly
- Avoids calculating prefix at positions that don't contribute to water (edges)
- Uses Python's functional `accumulate()` for clean code

**Example trace for [3, 0, 1, 0, 4, 0, 2]**:
```
arr:        [3, 0, 1, 0, 4, 0, 2]
           
Step 1: Build suffix_max using accumulate and reverse
reversed:   [2, 0, 4, 0, 1, 0, 3]
accumulate: [2, 2, 4, 4, 4, 4, 4]
reversed:   [4, 4, 4, 4, 4, 2, 2]  ← suffix_max (same as right array from Approach 2)

Step 2: Iterate and calculate on-the-fly
i=1: prefix_max=3, suffix_max[2]=4, min(3,4)-0 = 3 water, prefix_max becomes max(3,0)=3
i=2: prefix_max=3, suffix_max[3]=4, min(3,4)-1 = 2 water, prefix_max becomes max(3,1)=3
i=3: prefix_max=3, suffix_max[4]=4, min(3,4)-0 = 3 water, prefix_max becomes max(3,0)=3
i=4: prefix_max=3, suffix_max[5]=2, min(3,2)-4 = -2 → max(0,-2)=0 water, prefix_max becomes max(3,4)=4
i=5: prefix_max=4, suffix_max[6]=2, min(4,2)-0 = 2 water, prefix_max becomes max(4,0)=4

Total: 3 + 2 + 3 + 0 + 2 = 10 ✓
```

**Advantages**:
- Balanced space-time trade-off
- Uses Python's functional programming tools elegantly
- Single iteration for calculation phase
- Avoids unnecessary calculations at boundary positions

**Space Breakdown**:
- `suffix_max` array: O(n)
- `prefix_max` variable: O(1)
- Total: O(n) but with smaller constant factor than Approach 2

## Code Implementation Mapping

### C++ Implementation - Approach 1: Two-Pointer with Max Tracking

**File**: `solution.cpp`

**Key Features**:
- **Single-pass algorithm**: Processes array in one iteration only
- **Space-efficient**: Uses O(1) auxiliary space
- **Two pointers**: One from start (`left`), one from end (`right`)
- **Max tracking**: Maintains `left_max` and `right_max` as pointers move
- **Bottleneck principle**: Always processes the side with smaller height first

**Code Structure**:
```cpp
int maxWater(vector<int> &arr) {
    // 1. Initialize: left=0, right=size-1, left_max=0, right_max=0
    // 2. While left <= right:
    //    - If arr[left] <= arr[right]:
    //      - Update left_max if needed, else add trapped water
    //      - Move left pointer forward
    //    - Else:
    //      - Update right_max if needed, else add trapped water
    //      - Move right pointer backward
    // 3. Return total water trapped
}
```

**Why This Approach**:
- Best for **performance-critical** scenarios
- Optimal space usage
- Elegant solution that demonstrates advanced pointer manipulation
- Shows understanding of the core insight that smaller height is the bottleneck

### Python Implementation - Approach 2: Prefix-Suffix Maximum Arrays

**File**: `solution.py`

**Key Features**:
- **Two-phase algorithm**: Separate precomputation and calculation phases
- **Explicit arrays**: Stores all maximums explicitly for clarity
- **Forward iteration only**: Simple left-to-right and right-to-left scans
- **Clear logic separation**: Easy to understand and debug
- **Readability-first**: Prioritizes code clarity over space efficiency

**Code Structure**:
```python
def maxWater(self, arr):
    # Phase 1: Build left array - max height from start to each position
    #          Scan from left to right, store max encountered so far
    # 
    # Phase 2: Build right array - max height from each position to end
    #          Scan from right to left, store max encountered backward
    # 
    # Phase 3: Calculate water trapped
    #          For each position i: water += min(left[i], right[i]) - arr[i]
    # 
    # Return total water
```

**Why This Approach**:
- Best for **interviews and learning**
- Very intuitive and easy to explain
- Clear logical separation makes debugging straightforward
- Trades space (O(n)) for clarity
- Great teaching tool to understand the concept

### Python Implementation - Approach 3: Suffix-Max with On-the-Fly Prefix-Max

**Key Features**:
- **Single array precomputation**: Uses elegant `accumulate()` with `reversed()`
- **On-the-fly prefix calculation**: Maintains prefix_max during iteration
- **Balanced trade-off**: One array (suffix) + one variable (prefix)
- **Pythonic style**: Leverages functional programming tools
- **Efficient iteration**: Only processes middle elements (skips edges)

**Code Structure**:
```python
def maxWater(self, arr):
    # Build suffix_max using functional approach
    suffix_max = list(accumulate(reversed(arr), max))
    suffix_max.reverse()
    
    # Track prefix_max on-the-fly
    prefix_max = arr[0]
    water = 0
    
    # Iterate through middle elements only
    for i in range(1, len(arr) - 1):
        # Water at i uses suffix_max[i+1] (max to the right)
        # and prefix_max (max to the left so far)
        water += max(0, min(prefix_max, suffix_max[i + 1]) - arr[i])
        prefix_max = max(prefix_max, arr[i])
    
    return water
```

**Why This Approach**:
- **Best for** Python developers who understand functional programming
- **Elegant**: Uses built-in `accumulate()` for clean code
- **Balanced**: One precomputed array, one dynamic variable
- **Efficient**: Single calculation pass through middle elements
- **Shows Python mastery**: Demonstrates knowledge of functional tools

## Comparison of Implementations

| Aspect | C++ (Approach 1) | Python (Approach 2) | Python (Approach 3) |
|--------|------------------|-------------------|-------------------|
| **Strategy** | Two pointers from ends | Precompute all maximums | Precompute suffix, on-the-fly prefix |
| **Time Complexity** | O(n) | O(n) | O(n) |
| **Space Complexity** | O(1) | O(n) | O(n) |
| **Passes Required** | 1 | 3 | 2 |
| **Pointer Movement** | Convergent (towards center) | Sequential (L→R, R→L) | Sequential (R→L, then L→R) |
| **Arrays Used** | None | 2 (left, right) | 1 (suffix_max) + variable |
| **Logic Complexity** | High (conditional branching) | Low (straightforward loops) | Medium (functional + loop) |
| **Code Length** | Compact (45 lines with comments) | Medium (30 lines with comments) | Compact (10-15 lines) |
| **Clarity** | Requires thought | Immediately clear | Clear but functional style |
| **Best Use Case** | Production code, interviews | Learning, teaching | Code golf, elegance |
| **Interview Impact** | Shows mastery of pointers | Shows clear thinking | Shows Python knowledge |

## Complexity Analysis

### Approach 1: Two-Pointer (C++)

**Time Complexity: O(n)**
- Single pass through the array with two pointers
- Each element is visited exactly once
- Pointer movements combined traverse the entire array once

**Space Complexity: O(1)**
- Only uses a constant amount of extra space
- Variables: `left`, `right`, `left_max`, `right_max`, `water_trapped`
- No additional data structures

### Approach 2: Prefix-Suffix Maximum (Python)

**Time Complexity: O(n)**
- First loop: Build `left` array - O(n)
- Second loop: Build `right` array - O(n)
- Third loop: Calculate total water - O(n)
- Total: 3 × O(n) = O(n)

**Space Complexity: O(n)**
- Two auxiliary arrays: `left[n]` and `right[n]`
- Total space used: 2n = O(n)

## Comparison of Approaches

| Aspect | Approach 1 (Two-Pointer) | Approach 2 (Full Arrays) | Approach 3 (Hybrid) |
|--------|---------------------------|--------------------------|----------------------|
| **Time Complexity** | O(n) | O(n) | O(n) |
| **Space Complexity** | O(1) | O(n) | O(n) |
| **Passes** | 1 pass | 3 passes | 2 passes |
| **Readability** | Clever, requires understanding | Straightforward, explicit | Clean, uses functional style |
| **Precomputation** | None (on-the-fly) | Both arrays | Only suffix array |
| **Pointer Logic** | Complex (moving from ends) | Simple (forward iteration) | Mixed (functional + loop) |
| **Best For** | Space-critical problems | Interview clarity, learning | Python elegance |
| **Intuition** | Hard initially | Very intuitive | Medium (functional approach) |
| **Code Conciseness** | Brief but dense | Verbose but clear | Very concise |

## Use Cases

1. **Civil Engineering**: Calculating water retention in valleys and terrain models
2. **Environmental Science**: Analyzing water flow and accumulation in landscapes
3. **Data Structure Practice**: Common interview question for array manipulation
4. **Optimization Problems**: Finding maximum utilization of available space
5. **Reservoir Design**: Determining optimal water storage capacity
6. **Flood Simulation**: Modeling water accumulation in urban areas

## Advantages & Disadvantages

### Approach 1 (Two-Pointer)
✅ **Advantages**:
- Minimal space usage (O(1) auxiliary space)
- Single pass through array
- Optimal resource efficiency

❌ **Disadvantages**:
- Complex logic, hard to understand at first glance
- Requires careful pointer management
- Not ideal for learning phase

### Approach 2 (Prefix-Suffix)
✅ **Advantages**:
- Very intuitive and easy to understand
- Clear logical separation
- Straightforward to implement and debug
- Great for interviews and explanations

❌ **Disadvantages**:
- Uses O(n) extra space for arrays
- Three passes instead of one
- Not optimal for memory-constrained environments

## Edge Cases

1. **Empty array**: Return 0
2. **Single element**: Return 0 (no water can be trapped)
3. **Two elements**: Return 0 (need at least 3 for water trapping)
4. **Strictly increasing**: Return 0 (no valley to trap water)
5. **All same height**: Return 0 (flat surface)
6. **V-shaped array**: Maximum water can be trapped

## Key Takeaway

The fundamental insight is: **water trapped at each position depends on the minimum of the maximum heights on both sides**. You can either:
- Compute this on-the-fly with two pointers (space-efficient)
- Precompute all maximums (time-efficient and clearer)

