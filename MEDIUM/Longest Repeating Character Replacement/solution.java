class Solution {
    public int longestSubstr(String s, int k) {
        
         int[] freq=new int[26];
        int j=0;
        int maxfreq=0;
        int maxlen=0;
        int n= s.length();
        for(int i=0;i<n;i++)
        {
            freq[s.charAt(i)-'A']++;
            
            maxfreq=Math.max(maxfreq,freq[s.charAt(i)-'A']);
            
            while((i-j+1)-maxfreq>k)
            {
                freq[s.charAt(j)-'A']--;
                j++;
            }
            maxlen=Math.max(maxlen,i-j+1);
        }
        return maxlen;
    }
}