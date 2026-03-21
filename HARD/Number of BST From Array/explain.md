Approach:

1. Observation:
   - For any element chosen as root, the BST structure depends only on:
       → number of elements smaller than it (left subtree)
       → number of elements greater than it (right subtree)

   - Number of BSTs possible with k nodes = Catalan(k)

   - So for each element:
       answer = Catalan(left_count) * Catalan(right_count)

2. Optimization:
   - Instead of counting smaller/greater elements for each element in O(n),
     we sort the array.

   - After sorting:
       → index i represents the number of smaller elements
       → (n - i - 1) represents number of greater elements

3. Steps:
   - Store elements along with their original indices.
   - Sort based on values.
   - For each element in sorted array:
        smaller = i
        larger = n - i - 1
        compute result using precomputed Catalan numbers
   - Place result back using original index.

4. Complexity:
   - Sorting: O(n log n)
   - Traversal: O(n)
   - Overall: O(n log n)

5. Note:
   - Catalan numbers are precomputed up to n = 15 as per constraints.