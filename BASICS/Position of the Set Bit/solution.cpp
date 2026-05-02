class Solution {
  public:
    int findPosition(int n) {
        return (n & (n - 1)) ? -1 : (int)log2(n) + 1;
    }
};