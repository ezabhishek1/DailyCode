class Solution {
    String URLify(String s) {
        // code here
        String st=" ";
        
        for(int i=0;i<s.length();i++){
        char ch=s.charAt(i);
        if(ch ==' ')st+="%20";
        else
        st+=ch;
    }
        return st;
    }
}