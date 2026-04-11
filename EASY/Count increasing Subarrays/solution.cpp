class Solution {
  public:
    int countIncreasing(vector<int>& arr) {
        // code here.
        int p = 0;
        int ans = 0;
        
        for(int i=1;i<arr.size();i++){
            if(arr[i]<=arr[i-1])p=i;
            else ans += (i-p);
            
        }
        
        return ans;
    }
};