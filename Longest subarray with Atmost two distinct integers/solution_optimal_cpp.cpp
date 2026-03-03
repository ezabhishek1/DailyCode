#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    // ============================================================================
    // OPTIMAL C++ SOLUTION: Two Pointer + HashMap (At Most 2 Distinct Elements)
    // ============================================================================
    // Time Complexity: O(n) - Each element visited at most twice
    // Space Complexity: O(1) - HashMap stores at most 2 elements
    //
    // PROBLEM:
    // Find the length of the longest contiguous subarray with at most 2 distinct integers.
    //
    // APPROACH:
    // Use two pointers (i, j) forming a sliding window.
    // Maintain a map with at most 2 distinct elements.
    // Expand the window when valid, shrink when invalid.
    //
    // WHY THIS WORKS:
    // - The window [i, j] is valid if it has ≤ 2 distinct elements
    // - Adding arr[j] might make it invalid (3 distinct elements)
    // - We shrink from the left (move i) until we have ≤ 2 distinct again
    // - We never need to backtrack since we only care about longest window
    // - The answer is: max(j - i + 1) across all valid windows
    // ============================================================================
    
    int totalElements(vector<int> &arr) {
        if (arr.empty()) return 0;
        
        int n = arr.size();
        int i = 0;                           // Left pointer of sliding window
        int j = 0;                           // Right pointer of sliding window
        int maxLength = 0;                   // Track the maximum window length
        
        // HashMap to store frequency of elements in current window
        // Key: element value, Value: frequency count
        // Note: This will have at most 2 entries due to our constraint
        unordered_map<int, int> elementFreq;
        
        // ========================================================================
        // EXPAND AND SHRINK SLIDING WINDOW
        // ========================================================================
        // The for loop handles right pointer expansion
        for (j = 0; j < n; j++) {
            // Step 1: Add arr[j] to the window
            // Increment frequency of the element at position j
            elementFreq[arr[j]]++;
            
            // ====================================================================
            // SHRINK WINDOW IF CONSTRAINT IS VIOLATED
            // ====================================================================
            // While we have MORE than 2 distinct elements, shrink from left
            while (elementFreq.size() > 2) {
                // Decrement frequency of the leftmost element
                elementFreq[arr[i]]--;
                
                // If frequency becomes 0, the element is no longer in window
                // Remove it from the map to keep distinct count accurate
                if (elementFreq[arr[i]] == 0) {
                    elementFreq.erase(arr[i]);
                }
                
                // Move left pointer to the right (shrink window from left)
                i++;
            }
            
            // ====================================================================
            // UPDATE MAXIMUM LENGTH
            // ====================================================================
            // Now window [i, j] is valid (has at most 2 distinct elements)
            // Calculate window length and update maximum
            int currentLength = j - i + 1;
            maxLength = max(maxLength, currentLength);
            
            // Example: if i=2, j=5, then window = [2,3,4,5], length = 5-2+1 = 4
        }
        
        return maxLength;
    }
};

// ============================================================================
// DETAILED WALKTHROUGH EXAMPLE
// ============================================================================
/*
Array: [1, 2, 1, 2, 3]

Initial: i=0, j=-1, elementFreq={}, maxLength=0

j=0: Add arr[0]=1
     elementFreq={1:1}, size=1 ≤ 2 ✓ Valid
     length = 0-0+1 = 1, maxLength = 1
     State: Window=[1]

j=1: Add arr[1]=2
     elementFreq={1:1, 2:1}, size=2 ≤ 2 ✓ Valid
     length = 1-0+1 = 2, maxLength = 2
     State: Window=[1,2]

j=2: Add arr[2]=1
     elementFreq={1:2, 2:1}, size=2 ≤ 2 ✓ Valid
     length = 2-0+1 = 3, maxLength = 3
     State: Window=[1,2,1]

j=3: Add arr[3]=2
     elementFreq={1:2, 2:2}, size=2 ≤ 2 ✓ Valid
     length = 3-0+1 = 4, maxLength = 4
     State: Window=[1,2,1,2]

j=4: Add arr[4]=3
     elementFreq={1:2, 2:2, 3:1}, size=3 > 2 ✗ Invalid!
     
     SHRINK FROM LEFT:
     i=0: Remove arr[0]=1
          elementFreq[1]-- → {1:1, 2:2, 3:1}
          size=3 still > 2, continue shrinking
          i++ → i=1
     
     i=1: Remove arr[1]=2
          elementFreq[2]-- → {1:1, 2:1, 3:1}
          size=3 still > 2, continue shrinking
          i++ → i=2
     
     i=2: Remove arr[2]=1
          elementFreq[1]-- → {1:0, 2:1, 3:1}
          elementFreq[1]==0, so erase it → {2:1, 3:1}
          size=2 ≤ 2 ✓ Valid
          i++ → i=3
     
     length = 4-3+1 = 2, maxLength = max(4, 2) = 4
     State: Window=[2,3]

Loop ends (j reaches n-1)

ANSWER: maxLength = 4
The longest valid subarray is [1,2,1,2] with length 4

============================================================================
KEY INSIGHTS:
============================================================================
1. The map.size() directly gives us the count of distinct elements
2. When size > 2, we KNOW the constraint is violated
3. We shrink from the left because we want the LONGEST valid window
4. Once we shrink, we never backtrack left pointer - it only moves right
5. This guarantees O(n) time because each element is processed at most twice
6. Space is O(1) because map will never have more than 2 entries
7. The final answer is the maximum window size we found during traversal

============================================================================
WHY NOT USE OTHER DATA STRUCTURES?
============================================================================
- Array: Would need to know the range of values (not flexible)
- Set: Would work but we also need to count frequencies
- HashMap/Map: Perfect balance - tracks both distinct elements AND frequencies
- unordered_map: Faster average case, works well here
- map: Slightly slower but deterministic, good for interviews

============================================================================
COMPARISON WITH PYTHON VERSION:
============================================================================
This C++ approach is the "expand-first" method:
1. Expand window by adding arr[j]
2. Then shrink if needed using while loop
3. Update max after ensuring validity

The Python version uses "conditional movement":
1. Check if valid BEFORE moving
2. Different actions based on validity
3. Final check after loop

Both are O(n) and O(1), just different implementation styles.
C++ version: More direct, relies on while loop
Python version: More explicit, uses if/else branches

============================================================================
*/

// ============================================================================
// MAIN FUNCTION FOR TESTING
// ============================================================================
int main() {
    Solution sol;
    
    // Test Case 1
    vector<int> arr1 = {1, 2, 1, 2, 3};
    cout << "Input: [1, 2, 1, 2, 3]" << endl;
    cout << "Output: " << sol.totalElements(arr1) << endl;
    cout << "Expected: 4 (subarray [1,2,1,2])" << endl << endl;
    
    // Test Case 2
    vector<int> arr2 = {1, 2, 3, 4, 5};
    cout << "Input: [1, 2, 3, 4, 5]" << endl;
    cout << "Output: " << sol.totalElements(arr2) << endl;
    cout << "Expected: 2 (any two consecutive)" << endl << endl;
    
    // Test Case 3
    vector<int> arr3 = {1, 1, 1, 1};
    cout << "Input: [1, 1, 1, 1]" << endl;
    cout << "Output: " << sol.totalElements(arr3) << endl;
    cout << "Expected: 4 (entire array, only 1 distinct)" << endl << endl;
    
    // Test Case 4
    vector<int> arr4 = {0, 1, 2, 1, 0, 1, 3};
    cout << "Input: [0, 1, 2, 1, 0, 1, 3]" << endl;
    cout << "Output: " << sol.totalElements(arr4) << endl;
    cout << "Expected: 5 (subarray [0,1,2,1,0])" << endl;
    
    return 0;
}
