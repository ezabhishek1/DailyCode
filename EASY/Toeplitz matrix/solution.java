class Solution {
    public boolean isToeplitz(int[][] mat) {
        // code here
        int n=mat.length;
        int mm=mat[0].length;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<mm;j++){
                if(mat[i][j]==-1) continue;
                int num=mat[i][j];
                int r=i+1;
                int m=j+1;
                while(r>=0 && r<n && m>=0 && m<mm){
                    if(num!=mat[r][m]) return false;
                    mat[r][m]=-1;
                    r++;
                    m++;
                }
            }
        }
        
        return true;
    }
}