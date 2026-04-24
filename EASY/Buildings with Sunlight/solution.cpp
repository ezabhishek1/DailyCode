class Solution {
  public:
    int visibleBuildings(vector<int>& arr) {
        // code here
        int maxi = 0;
        int count = 0;
        
        for (int x : arr) {
            
            if (x >= maxi) {
                count++;
            }
            
            maxi = max(maxi, x);
        }
        
        return count;
    }
};