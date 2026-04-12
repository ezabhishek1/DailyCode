class Solution {
  private:
    bool calc(vector<vector<int>>& arr, int i, int j, int n, int m) {
        int data = arr[i][j];
        i++;
        j++;
        while (i < n && j < m) {
            if (arr[i][j] != data)
                return false;
            i++;
            j++;
        }
        return true;
    }
  public:
    bool isToeplitz(vector<vector<int>>& matrix) {
        // code here
        int n = matrix.size(), m = matrix[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!calc(matrix, i, j, n, m))
                    return false;
            }
        }
        return true;
    }
};