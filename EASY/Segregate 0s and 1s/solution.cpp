class Solution {
  public:
    void segregate0and1(vector<int> &arr) {
        // code here
        int c0 = count(arr.begin(), arr.end(), 0);
        int n = arr.size();
        for (int i = 0; i < n; i++){
            if (c0 > 0){
                arr[i] = 0;
                c0--;
            }
            else arr[i] = 1;
        }
    }
};