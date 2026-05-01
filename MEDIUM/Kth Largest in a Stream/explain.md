# Approach

I maintain a min-heap (priority queue) that holds at most K elements at any time.

For each element in the array, I push it into the heap. If the heap size exceeds K, I pop the top (the smallest element in the heap). After this operation, the heap always contains the K largest elements seen so far, and the top of the heap is the Kth largest. If the heap has fewer than K elements, I push -1 into the result instead.




# Using minHeap ...
## => DRY RUN TO UNDERSTAND
    vector<int> kthLargest(int k, int arr[], int n) {
        vector<int>ans(n,-1);
        priority_queue<int, vector<int>, greater<int>>p;
        
        for(int i=0; i<k; i++)
            p.push(arr[i]);
        
        bool flag = 0;
        for(int i=k-1; i<n; i++){
            if(flag && p.top() < arr[i]){
                p.pop();
                p.push(arr[i]);
            }
            flag = 1;
            ans[i] = p.top();
        }
        
        return ans;
    }