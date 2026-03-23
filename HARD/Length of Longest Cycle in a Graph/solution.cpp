class Solution {
  public:
    int longestCycle(int V, vector<vector<int>>& edges) {
        // code here
        vector<pair<int,int>>vis(V,{-1,-1});
        unordered_map<int,int>mp;
        int ans=-1;
        
        for(auto it:edges){
            mp[it[0]]=it[1];
            if(it[0]==it[1]) ans=1;
        } 
        
        for(int i=0;i<V;i++){
            if(vis[i].first!=-1) continue;
            
            int t=i;
            int cnt=0;
            while(vis[t].first==-1){
                
                vis[t].first=cnt;
                vis[t].second=i;
                if(mp.find(t)!=mp.end())
                    t=mp[t];
                else break;
                cnt++;
            }
           if(vis[t].second==i) ans=max(ans,cnt-vis[t].first);
           
        }
        return (ans)?ans:-1;
    }
};