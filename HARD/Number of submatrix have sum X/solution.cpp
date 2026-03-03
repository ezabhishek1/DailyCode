class Solution {
public:
    int countSquare(vector<vector<int>>& mat, int x) {
        // ═══════════════════════════════════════════════════════════════
        // APPROACH: 2D Prefix Sum for O(1) Range Queries
        // ═══════════════════════════════════════════════════════════════
        // Key: Precompute prefix sums to get any submatrix sum in O(1)
        // using the 2D inclusion-exclusion formula
        // ═══════════════════════════════════════════════════════════════
        
        int n = mat.size(), m = mat[0].size();
        int count = 0;
        
        // Use long long to prevent overflow
        vector<vector<long long>> pre(n + 1, vector<long long>(m + 1, 0));
        
        // Build 2D prefix sum: O(n × m)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                pre[i+1][j+1] = mat[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j];
            }
        }
        
        // Lambda for efficient range sum query: O(1)
        auto getSum = [&](int r1, int c1, int r2, int c2) -> long long {
            return pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1];
        };
        
        // Enumerate all square submatrices: O(n × m × min(n, m))
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // For each size k (where square is (k+1) × (k+1))
                for (int k = 0; i + k < n && j + k < m; k++) {
                    if (getSum(i, j, i + k, j + k) == x) {
                        count++;
                    }
                }
            }
        }
        
        return count;
    }
};

/*
═══════════════════════════════════════════════════════════════
COMPLEXITY ANALYSIS
═══════════════════════════════════════════════════════════════

Time Complexity: O(n × m × min(n, m)) or O(n³) for square matrix
  - Prefix sum computation: O(n × m)
  - Square enumeration:
    * Positions: n × m
    * Sizes: up to min(n, m)
    * Per-check: O(1)
    * Total: O(n × m × min(n, m))

Space Complexity: O(n × m)
  - Prefix array: (n+1) × (m+1)

Key Formula (2D Inclusion-Exclusion):
  sum(r1,c1,r2,c2) = pre[r2+1][c2+1]   // include all
                    - pre[r1][c2+1]     // exclude top
                    - pre[r2+1][c1]     // exclude left
                    + pre[r1][c1]       // restore corner

Why Prefix Sum is Essential:
  Without: O(n⁵) brute force (recalculate sum for each square)
  With:    O(n³) optimized (O(1) lookup per square)
  
═══════════════════════════════════════════════════════════════
*/

// ═══════════════════════════════════════════════════════════════
// APPROACH 2: Optimized Square Size Enumeration
// ═══════════════════════════════════════════════════════════════
/*
🔷 Core Strategy

This approach elegantly combines two key observations:

1. **2D Prefix Sum Construction**
   Build a 2D prefix sum array that allows O(1) computation of
   any rectangular region sum using the inclusion-exclusion principle.
   
   Why? Enables rapid queries without recalculating element sums.

2. **Systematic Square Enumeration**
   Iterate through all possible:
   - Top-left positions (i, j)
   - Square sizes k (where size = k+1)
   
   Count those with sum exactly equal to x.

🔹 Why This Approach is Effective

✓ Comprehensive Check: Examines all possible square submatrices
✓ Efficient Queries: O(1) per submatrix due to prefix sums
✓ Passes All Edge Cases:
  - Single-element squares
  - Full matrix as square
  - Negative numbers
  - Zero values
  - Duplicate target sums

🔹 Detailed Algorithm Step-by-Step

Step 1: Build 2D Prefix Sum Array (Pass 1 through matrix)
  for i from 1 to n:
    for j from 1 to m:
      pre[i][j] = mat[i-1][j-1] 
                + pre[i-1][j] 
                + pre[i][j-1] 
                - pre[i-1][j-1]

Step 2: Enumerate All Square Submatrices (Pass 2 through matrix)
  for i from 0 to n-1:          // top-left row
    for j from 0 to m-1:        // top-left column
      for k from 0 to min(n,m): // square size (k+1)×(k+1)
        if i+k < n and j+k < m:
          sum = getSum(i, j, i+k, j+k)
          if sum == x:
            count++

Step 3: Return Total Count

🔷 Why All Test Cases Pass

Edge Case Coverage:
  ✓ 1×1 squares: Handled by k=0
  ✓ Full matrix: Handled when k = min(n,m)-1
  ✓ Boundary squares: No buffer zones, all checked
  ✓ Negative sums: Prefix formula works with any numbers
  ✓ Duplicate matches: All are counted separately
  ✓ No match case: Returns 0 correctly

Performance Guarantees:
  ✓ No TLE (Time Limit Exceeded): O(n³) is acceptable for n ≤ 100
  ✓ No overflow: Use long long for intermediate sums
  ✓ No off-by-one errors: 1-based prefix, 0-based enumeration

🔷 Visual Walkthrough

Matrix (3×3), x = 12:
┌─────────────┐
│ 1 │ 2 │ 3 │
├─────────────┤
│ 4 │ 5 │ 6 │
├─────────────┤
│ 7 │ 8 │ 9 │
└─────────────┘

Prefix Array:
0   0   0   0
0   1   3   6
0   5  12  21
0  12  27  45

Check all squares:
─────────────────
Size 1×1:
  (0,0)→(0,0): pre[1][1] = 1 ❌
  (0,1)→(0,1): pre[1][2] - pre[1][1] = 2 ❌
  ... (no matches)

Size 2×2:
  (0,0)→(1,1): pre[2][2] - pre[0][2] - pre[2][0] + pre[0][0]
             = 12 - 0 - 0 + 0 = 12 ✓ COUNT=1
             (matches: 1+2+4+5=12)
             
  (0,1)→(1,2): pre[2][3] - pre[0][3] - pre[2][1] + pre[0][1]
             = 21 - 0 - 5 + 0 = 16 ❌
             
  (1,0)→(2,1): pre[3][2] - pre[1][2] - pre[3][0] + pre[1][0]
             = 27 - 3 - 0 + 0 = 24 ❌
             
  (1,1)→(2,2): pre[3][3] - pre[1][3] - pre[3][1] + pre[1][1]
             = 45 - 6 - 12 + 1 = 28 ❌

Size 3×3:
  (0,0)→(2,2): entire matrix = 45 ❌

ANSWER: 1 (only the 2×2 at top-left sums to 12)

🔷 Why This is Optimal

Compared to Alternatives:

Brute Force (no prefix):
  Recalculate each sum: O(size²) per check
  Total: O(n² × m² × k²) = O(n⁵)
  ❌ Too slow for n > 20

With Prefix Sum:
  Precompute: O(nm)
  Each check: O(1)
  Total: O(n × m × min(n,m)) = O(n³)
  ✓ Fast enough for n ≤ 500

HashMap Variant:
  Could optimize if x is very rare
  But prefix sum is simpler and sufficient
  ✓ Good balance of simplicity and speed

🔷 Implementation Considerations

1. Data Types:
   - Use long long for prefix array (prevent overflow)
   - Use int for indices
   - int for count (at most n² submatrices)

2. Boundary Handling:
   - 1-based indexing in prefix array simplifies logic
   - 0-based indexing for matrix iteration is standard
   - Formula handles all boundaries automatically

3. Loop Conditions:
   - Outer loops: standard iteration (i, j)
   - Inner loop: k goes until square exceeds boundaries
   - Condition: i+k < n && j+k < m

═══════════════════════════════════════════════════════════════
*/