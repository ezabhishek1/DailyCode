class Solution {
    public int findPosition(int n) {
        int lsb = n & ~(n-1);
        if(lsb != n) return -1;
        return 32-Integer.numberOfLeadingZeros(lsb);
    }
}