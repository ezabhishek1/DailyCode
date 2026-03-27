class Solution {
  public:
    int solve(int n, int m, vector<vector<int>>& grid) {
        vector<vector<int>> front(m, vector<int>(m, 0));
        for(int i=0;i<m;i++){
            for(int j=0;j<m;j++){
                if(i==j) front[i][j]=grid[n-1][i];
                else front[i][j]=grid[n-1][i]+grid[n-1][j];
            }
        }
        
        for(int i=n-2;i>=0;i--){
            vector<vector<int>> cur(m, vector<int>(m, 0));
            for(int j1=0;j1<m;j1++){
                for(int j2=0;j2<m;j2++){
                    int maxi=-1e8;
                    for(int di=-1;di<=1;di++){
                        for(int dj=-1;dj<=1;dj++){
                            if(j1+di<0 || j2+dj<0 || j1+di>=m || j2+dj>=m) continue;
                            int val=0;
                            if(j1==j2) val=grid[i][j1];
                            else val=grid[i][j2]+grid[i][j1];
                            val+=front[j1+di][j2+dj];
                            maxi=max(maxi,val);
                        }
                    }
                    cur[j1][j2]=maxi;
                }
            }
            front=cur;
        }

       return front[0][m - 1];
        
    }
};