class Solution {
    public boolean isBinaryPalindrome(int n) {
        // code here
       String bin = Integer.toBinaryString(n);
       
       int l= 0;
       int r = bin.length() - 1;
       
       while( l < r){
           if(bin.charAt(l) != bin.charAt(r)){
               return false;
           }
           l++;
           r--;
       }
       return true;
    }
}