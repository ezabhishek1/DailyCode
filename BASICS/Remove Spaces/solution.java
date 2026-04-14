class Solution {
    String removeSpaces(String s) {
        // code here
        StringBuilder sb = new StringBuilder("");
        int n = s.length();
        for(int i = 0 ; i < n ; i++){
            if(s.charAt(i) != ' '){
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}