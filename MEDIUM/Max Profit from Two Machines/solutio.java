class Solution {
    public int maxProfit(int x, int y, int[] a, int[] b) {
        // code here
         int n = a.length;

        List<Integer> gain = new ArrayList<>();

        int profit = 0;

        // Initially all tasks assigned to B
        for (int i = 0; i < n; i++) {
            profit += b[i];
            gain.add(a[i] - b[i]);
        }

        // Sort gains descending
        Collections.sort(gain, Collections.reverseOrder());

        // At least (n - y) tasks must go to A
        int needA = n - y;

        // Pick top x gains
        for (int i = 0; i < x; i++) {

            // Forced OR beneficial
            if (i < needA || gain.get(i) > 0) {
                profit += gain.get(i);
            }
        }

        return profit;
    }
}