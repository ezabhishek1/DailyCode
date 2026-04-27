class Solution {
    public int smallestSubstring(String S) {
        
        int zero=-1,one=-1,two=-1,res,e,s;
        int len=(int)1e9;
        
        for(int i=0;i<S.length();i++)
        {
            if(S.charAt(i)=='0')
               zero=i;
            else if(S.charAt(i)=='1')
               one=i;
            else
               two=i;
               
            if(zero!=-1 && one!=-1 && two!=-1)
            {
                e=Math.max(zero,Math.max(one,two));
                s=Math.min(zero,Math.min(one,two));
                len=Math.min(len,e-s+1);
            }
        }
        res=(len>=1e9)?-1:len;
        return res;
        
    }
};