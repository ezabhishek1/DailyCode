class Solution {
    public ArrayList<Integer> findMean(int[] arr, int[][] queries) {
        // code here
        
        ArrayList<Integer> list = new ArrayList<>();
        int n=arr.length;
        int prefixarray[]=new int[n];
        int sum=0;
        for(int i=0;i<n;i++){
            sum=sum+arr[i];
            prefixarray[i]=sum;
        }
        
        for(int i=0;i<queries.length;i++){
            int l=queries[i][0];
            int r=queries[i][1];
            sum=prefixarray[r];
            if(l>0)
            sum=sum-prefixarray[l-1];
            
           
            int res=sum/(r-l+1);
            list.add(res);
        }
        return list;
    }
}