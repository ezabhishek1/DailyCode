class Solution {
  public:
    vector<int> commonElements(vector<int> &a, vector<int> &b, vector<int> &c) {
        vector<int> ans;
        int i = 0, j = 0, k = 0;

        while (i < (int)a.size() && j < (int)b.size() && k < (int)c.size()) {
            int x = a[i], y = b[j], z = c[k];

            if (x == y && y == z) {
                if (ans.empty() || ans.back() != x) {
                    ans.push_back(x);
                }
                i++;
                j++;
                k++;
            }
            else {
                int mn = min(x, min(y, z));
                if (x == mn) i++;
                if (y == mn) j++;
                if (z == mn) k++;
            }
        }

        return ans;
    }
};