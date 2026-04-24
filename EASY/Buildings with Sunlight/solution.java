class Solution {
    public int visibleBuildings(int arr[]) {
        // code here
        int ans=1;
        int first=arr[0];
        for(int i=1;i<arr.length;i++){
            if(arr[i]>=first){
                ans++;
                first=arr[i];
            }
        }
        
        return ans;
    }
}