class Solution {
    public ArrayList<Integer> commonElements(int[] a, int[] b, int[] c) {
        // code here
        int aLen = a.length;
        int bLen = b.length;
        int cLen = c.length;
        
        int i = 0 ;
        int j = 0 ;
        int k = 0;
        
        ArrayList<Integer> res = new ArrayList<>();
        
        while(i < aLen && j < bLen && k < cLen){
            if(a[i] <= b[j] && a[i] < c[k]){
                i++;
            }else if(b[j] < a[i] && b[j] <= c[k]){
                j++;
            }else if(c[k] <= a[i] && c[k] < b[j]){
                k++;
            }else {
                if(res.isEmpty()){
                    res.add(a[i]);
                }else if(res.get(res.size() - 1) != a[i]){
                    res.add(a[i]);
                }
                i++;
                j++;
                k++;
            }
        }
        return res;
    }
}