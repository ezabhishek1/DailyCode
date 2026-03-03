# Number of Submatrices with Sum Equal to X

## Problem Statement
Given a 2D matrix `mat` of size `n × m` and an integer `x`, count the **total number of square submatrices** whose sum equals `x`.

A square submatrix is defined by:
- A starting position (top-left corner)
- A size (width = height)
- All elements within this square region

### Examples
```
Matrix:
[  1  2  3 ]
[  4  5  6 ]
[  7  8  9 ]

x = 5

Answer: 1
Submatrices: [1×1 at (1,1) with value 5]

---

Matrix:
[  1  0 ]
[ -1  1 ]

x = 1

Answer: 2
Submatrices:
  - [1×1 at (0,0) with value 1]
  - [1×1 at (1,1) with value 1]
  - [2×2 entire matrix: 1 + 0 + (-1) + 1 = 1]
Total: 3
```

## Core Idea

### 2D Prefix Sum Technique
Transform the problem using a **2D prefix sum array**:

```
prefix[i][j] = sum of all elements in rectangle from (0,0) to (i-1,j-1)
```

#### Prefix Sum Construction
```
prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
```

The subtraction accounts for the overlap counted twice.

#### Range Sum Query
For any rectangle from (r1,c1) to (r2,c2):
```
sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
```

### Why This Works
- Without prefix sum: checking each submatrix takes **O(size²)** to compute sum
- With prefix sum: checking each submatrix takes **O(1)** to compute sum
- This reduces overall complexity from **O(n³m³)** to **O(n²m²)**

## Algorithm Approach

1. **Build 2D Prefix Sum**: Construct the prefix sum array
2. **Enumerate All Squares**: Iterate through:
   - All possible top-left positions (i, j)
   - All possible square sizes k
   - So submatrix is from (i, j) to (i+k, j+k)
3. **Query Sum Efficiently**: Use prefix array to get submatrix sum in O(1)
4. **Count Matches**: If sum equals x, increment counter
5. **Return Count**: Total number of matching submatrices

### Dry Run Example
```
Matrix:
[  1  2 ]
[  3  4 ]

x = 5

Step 1: Build Prefix Sum
prefix[0][0] = 0,  prefix[0][1] = 0,  prefix[0][2] = 0
prefix[1][0] = 0,  prefix[1][1] = 1,  prefix[1][2] = 3
prefix[2][0] = 0,  prefix[2][1] = 4,  prefix[2][2] = 10

Step 2: Check All Squares

Size 1 (1×1):
  - (0,0): sum = prefix[1][1] - prefix[0][1] - prefix[1][0] + prefix[0][0] = 1 ❌
  - (0,1): sum = prefix[1][2] - prefix[0][2] - prefix[1][1] + prefix[0][1] = 2 ❌
  - (1,0): sum = prefix[2][1] - prefix[1][1] - prefix[2][0] + prefix[1][0] = 3 ❌
  - (1,1): sum = prefix[2][2] - prefix[1][2] - prefix[2][1] + prefix[1][1] = 4 ❌

Size 2 (2×2):
  - (0,0): sum = prefix[2][2] - prefix[0][2] - prefix[2][0] + prefix[0][0] = 10 ❌

Answer: 0 (no submatrix sums to 5 in this example)
```

## Complexity Analysis

### Time Complexity: **O(n² × m²)** or **O(n³)** for square matrices

**Breakdown**:
- Building prefix sum: **O(n × m)**
- Enumerating all square submatrices:
  - Number of top-left positions: O(n × m)
  - Number of possible sizes: O(min(n, m))
  - For each combination: O(1) to compute sum
  - Total: O(n × m × min(n, m))
- **Overall**: O(n × m) + O(n × m × min(n, m)) = **O(n × m × min(n, m))**

If n = m (square matrix):
- Simplified: **O(n³)**

### Space Complexity: **O(n × m)**
- Prefix sum array: (n+1) × (m+1) = **O(n × m)**
- No additional data structures needed
- Input matrix is not modified (or counted separately)

## Use Cases

### 1. **Image Processing & Computer Vision**
   - Detecting regions in images with specific brightness sum
   - Finding areas of uniform intensity
   - Rapid computation of integral images for feature detection
   - Haar cascade classifier computation
   - Viola-Jones face detection preprocessing

### 2. **Financial Data Analysis**
   - Stock trading: finding time windows with specific profit/loss sums
   - Portfolio analysis: identifying periods with specific returns
   - Risk assessment: querying cumulative returns over matrix regions
   - Market segment analysis: analyzing trends in 2D grids

### 3. **Sensor Networks & IoT**
   - Aggregating sensor readings in grid-based deployments
   - Finding regions with specific total sensor output
   - Environmental monitoring: areas with specific pollution/temperature sums
   - Grid-based sensor mapping in smart cities

### 4. **Data Mining & Analytics**
   - Pattern detection in 2D datasets
   - Cluster analysis on grid-structured data
   - Finding subregions with specific aggregate values
   - Heatmap analysis for anomaly detection

### 5. **Game Development**
   - Pathfinding with cumulative cost matrices
   - Damage/healing calculations over map regions
   - Resource distribution across game board sections
   - Collision detection preprocessing

### 6. **Geographical Information Systems (GIS)**
   - Finding regions with specific population/land-use sums
   - Climate data analysis over geographic grids
   - Urban planning: areas with specific development metrics
   - Agricultural analysis: crop yield analysis by region

### 7. **Database Query Optimization**
   - Rapidly computing aggregates over matrix-indexed tables
   - OLAP (Online Analytical Processing) cube queries
   - Data warehouse range aggregations
   - Multidimensional indexing

### 8. **Document Analysis**
   - Feature extraction from scanned documents
   - Handwriting analysis: finding regions with specific ink density
   - Page segmentation: identifying sections with specific content density
   - OCR preprocessing

### 9. **Bioinformatics**
   - Analyzing 2D protein structure matrices
   - DNA sequence matching in 2D grid representations
   - Gene expression data analysis
   - Phylogenetic heat map analysis

### 10. **Manufacturing & Quality Control**
   - Detecting defect regions in manufacturing grids
   - PCB (Printed Circuit Board) defect detection
   - Quality metrics analysis over production units
   - Material property analysis over sample regions

### 11. **Traffic & Urban Systems**
   - Finding road segments with specific traffic volume sums
   - Congestion analysis over city grid sections
   - Parking availability analysis
   - Route optimization with cumulative costs

### 12. **Machine Learning & Neural Networks**
   - Convolution operations preprocessing
   - Feature map analysis in CNNs
   - Gradient computation over regions
   - Attention mechanism computation over spatial dimensions

## Visual Example

```
Matrix (4×4):
┌─────────────────────┐
│  1 │  2 │  3 │  4  │
├─────────────────────┤
│  5 │  6 │  7 │  8  │
├─────────────────────┤
│  9 │ 10 │ 11 │ 12  │
├─────────────────────┤
│ 13 │ 14 │ 15 │ 16  │
└─────────────────────┘

Find all square submatrices with sum = 34

Size 1: No matches (all single elements < 34)

Size 2: Checking [2,3,6,7], [3,4,7,8], [6,7,10,11], etc.
  [1,2,5,6]     = 14 ❌
  [2,3,6,7]     = 18 ❌
  [3,4,7,8]     = 22 ❌
  [5,6,9,10]    = 30 ❌
  [6,7,10,11]   = 34 ✓ (MATCH!)
  [7,8,11,12]   = 38 ❌
  [Continue checking...]

Size 3, Size 4: Check other combinations...

Answer: Count of all matching submatrices
```

## Algorithm Intuition

The power of this approach lies in **decoupling enumeration from summing**:

1. **Brute Force Approach**:
   ```
   For each top-left (i, j):
     For each size k:
       For each element in submatrix:
         Add to sum
       Check if sum == x
   Time: O(n² × m² × min(n,m)) or O(n⁵) worst case
   ```

2. **Optimized Approach** (with prefix sum):
   ```
   Precompute prefix sum: O(n × m)
   For each top-left (i, j):
     For each size k:
       Get sum in O(1) using prefix array
       Check if sum == x
   Time: O(n × m × min(n,m)) or O(n³) for square matrices
   ```

The prefix sum array trades **O(n × m) space** for significant **time savings**.

## Comparison: Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (recalculate sums) | O(n²m²×min(n,m)) | O(1) | Impractical for large matrices |
| **Prefix Sum** | **O(n³) or O(n²m²)** | **O(nm)** | **Optimal balance** |
| Advanced (HashMap + Optimization) | O(n²m²) with pruning | O(nm) | Better average case if target is rare |

## Implementation Notes

1. **1-based Indexing**: Prefix array uses 1-based indexing for easier boundary handling
2. **Data Types**: Use `long long` to handle overflow with large matrices
3. **Early Termination**: Can optimize by skipping sizes that exceed remaining matrix
4. **Memory Trade-off**: Prefix array doubles space, but reduces time significantly
5. **Optimization Opportunity**: If looking for maximum frequency target, HashMap can help prune search space

## Code Optimization Variations

### Approach 1: Nested Loops (C++)
Most straightforward, clear logic flow.

### Approach 2: Python Dictionary-based
Slightly more Pythonic, same complexity.

### Approach 3: Lambda Functions (C++)
Clean syntax, avoids code duplication for range sum queries.

## Conclusion

Counting submatrices with a specific sum is a classic **2D prefix sum** problem. This technique elegantly transforms the problem from O(n⁵) brute force to **O(n³)** for square matrices with efficient O(1) per-query lookups. The approach generalizes to any rectangular submatrices and has extensive applications in image processing, data analysis, GIS, and optimization problems. The key insight is recognizing that **precomputation of prefix sums** enables rapid range queries, making the problem tractable for real-world matrix sizes.   