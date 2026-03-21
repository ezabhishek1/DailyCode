Approach:

1. Observation:
   - For any element chosen as root, the BST structure depends only on:
       → number of elements smaller than it (left subtree)
       → number of elements greater than it (right subtree)

   - Number of BSTs possible with k nodes = Catalan(k)

   - So for each element:
       answer = Catalan(left_count) * Catalan(right_count)