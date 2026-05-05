class Solution {
  public:
    long long sumXOR(vector<int> &arr) {
        // code here
        int n = arr.size();
        long long ans = 0;
        for(int bit = 0; bit < 18; bit++) {
            int setCount = 0;
            for(int num : arr) {
                setCount += (num & (1 << bit)) > 0;
            }
            int unsetCount = n - setCount;
            ans += (1ll << bit) * setCount * unsetCount;
        }
        return ans;
    }
};