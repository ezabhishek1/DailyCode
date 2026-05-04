class Solution {
     public ArrayList<Integer> sortBySetBitCount(int[] arr) {
        int n = arr.length;

        // Convert to Integer[]
        Integer[] temp = new Integer[n];
        for (int i = 0; i < n; i++) {
            temp[i] = arr[i];
        }

        // Stable sort
        Arrays.sort(temp, (a, b) -> {
            return Integer.bitCount(b) - Integer.bitCount(a);
        });

        // Convert to ArrayList
        ArrayList<Integer> result = new ArrayList<>();
        for (int num : temp) {
            result.add(num);
        }

        return result;
    }
}