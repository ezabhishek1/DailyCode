class Solution {
    public ArrayList<Integer> search(int[] a, int[] b) {
        int n = a.length,m = b.length;
        int base = 256,md=100000007;
        long pathhash=0,texthash=0,power=1;
        for(int i=0;i<m-1;i++){
            power = (power*base)%md;
        }
        for(int i=0;i<m;i++){
            pathhash = (pathhash*base + a[i])%md;
            texthash = (texthash*base + b[i])%md;
        }
        ArrayList<Integer>ans = new ArrayList<Integer>();
        for(int i=0;i<n-m;i++){
            if(texthash==pathhash)ans.add(i);
            pathhash = (pathhash-(a[i]*power)%md+md)%md;
            pathhash = (pathhash*base + a[i+m])%md;
        }
        if(texthash==pathhash)ans.add(n-m);
        return ans;
    }
}