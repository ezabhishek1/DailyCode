class Solution {
  public:
    vector<int> nextPalindrome(vector<int>& num) {
        int n = num.size();

        bool allNine = true;
        for (int x : num) {
            if (x != 9) {
                allNine = false;
                break;
            }
        }
        if (allNine) {
            vector<int> ans(n + 1, 0);
            ans[0] = 1;
            ans[n] = 1;
            return ans;
        }

        int i = (n - 1) / 2;
        int j = n / 2;

        while (i >= 0 && num[i] == num[j]) {
            i--;
            j++;
        }

        bool leftSmaller = (i < 0 || num[i] < num[j]);

        i = (n - 1) / 2;
        j = n / 2;
        while (i >= 0) {
            num[j] = num[i];
            i--;
            j++;
        }

        if (leftSmaller) {
            int carry = 1;
            i = (n - 1) / 2;
            j = n / 2;

            while (i >= 0 && carry) {
                int val = num[i] + carry;
                num[i] = val % 10;
                carry = val / 10;
                num[j] = num[i];
                i--;
                j++;
            }
        }

        return num;
    }
}; 