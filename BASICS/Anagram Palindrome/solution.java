class Solution {
    boolean canFormPalindrome(String s) {
        // code here
        int n=s.length();
        int a[]=new int[26];
        int o=0;
        for(char x:s.toCharArray()){
            a[x-'a']++;
            if(a[x-'a']%2!=0)
                o++;
            else
                o--;
        }
        if(n%2!=0 && o==1 || n%2==0 && o==0)
            return true;
        return false;
    }
}