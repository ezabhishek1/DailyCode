class Solution {
    public int minSwaps(int[] arr) {
        // code here
        int n =  arr.length;
        int k = 0;
        for(int i = 0;i<n;i++){
            if(arr[i]==1){
                k++;
            }
        }
        if(k==0)return -1;
        int windoFirstOnes = 0;
        for(int i = 0;i<k;i++){
            if(arr[i]==1){
                 windoFirstOnes++;
            }
        }
        int maxOnes =  windoFirstOnes;
        for(int i = k;i<n;i++){
             windoFirstOnes+=arr[i];
              windoFirstOnes-=arr[i-k];
              maxOnes = Math.max(maxOnes, windoFirstOnes);
        }
        return k-maxOnes;
    }
}