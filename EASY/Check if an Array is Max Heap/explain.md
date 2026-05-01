Approach
I go through the array and treat each element as a parent node.

For every index i:

I calculate the left child index → 2*i + 1

I calculate the right child index → 2*i + 2

Then I check:

If left child exists and arr[i] < arr[left], then it's not a max heap

If right child exists and arr[i] < arr[right], then it's not a max heap

If I find even one violation, I return false immediately.

If I finish checking all nodes without any issue, then it is a valid max heap.

One small optimization I realized: I only need to check till n/2 - 1, because beyond that all nodes are leaf nodes and don’t have children.