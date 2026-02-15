class Solution {
public:
    int getCount(int n, int d) {
        // code here
        int l = 1;
        int r = n;
        while (l <= r) {
            int mid = (l + r) / 2;
            int number = mid;
            int sum = 0;
            while (number > 0) {
                sum += number % 10;
                number = number / 10;
            }
            if (mid - sum < d) {
                l = mid + 1;
            } else
                r = mid - 1;
        }
        return n - l + 1;
    }
};