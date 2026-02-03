##The change of direction is not necessary to be performed as at last there will be ants moving in both directions.Simply we need to find the ant which was away from end of the plank.


class Solution {
  public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int ans = 0;
        for (int num : left) {
            ans = max(ans, num);
        }
        for (int num : right) {
            ans = max(ans, n - num);
        }
        return ans;
    }
};