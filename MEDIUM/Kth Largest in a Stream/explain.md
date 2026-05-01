# Approach

I maintain a min-heap (priority queue) that holds at most K elements at any time.

For each element in the array, I push it into the heap. If the heap size exceeds K, I pop the top (the smallest element in the heap). After this operation, the heap always contains the K largest elements seen so far, and the top of the heap is the Kth largest. If the heap has fewer than K elements, I push -1 into the result instead.