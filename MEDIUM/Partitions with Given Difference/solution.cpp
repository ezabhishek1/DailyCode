class Solution {
  private:
    int perfectSum(vector<int>& arr, int target) {
        int n = arr.size();
        vector<int> prev(target+1, 0), cur(target+1, 0);
        
        if(arr[0] == 0) prev[0] = 2;
        else prev[0] = 1;
        if(arr[0] != 0 && arr[0] <= target) prev[arr[0]] = 1;
        
        for(int ind = 1; ind<n; ind++){
            for(int sum = 0; sum <= target; sum++){
                int notTake = prev[sum];
                int take = 0;
                if(arr[ind] <= sum) take = prev[sum - arr[ind]];
                
                cur[sum] = notTake + take;
            }
            prev = cur;
        }
        return prev[target];
    }
  public:
    int countPartitions(vector<int>& arr, int d) {
        int totSum = 0;
        for(auto &it: arr) totSum += it;
        if(totSum - d < 0 || (totSum - d)%2 != 0) return 0;
        return perfectSum(arr, (totSum - d)/2);
    }
};