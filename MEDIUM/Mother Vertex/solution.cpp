

class Solution {
  public:
    int findMotherVertex(int V, vector<vector<int>>& edges) {
        // code here
        vector<vector<int>> adj(V);
        for(const auto& it : edges)
        {
            adj[it[0]].push_back(it[1]);
        }
        vector<bool> vis(V,false);
        
        function<void(int)> dfs = [&](int node)
        {
            vis[node] = true;
            for(const auto& adjNode : adj[node])
            {
                if(!vis[adjNode])
                dfs(adjNode);
            }
        };
        int candidate = 0;
        for(int i= 0;i<V;i++)
        {
            if(!vis[i])
            {
                dfs(i);
                candidate = i;
            }
        }
        fill(vis.begin(), vis.end(),false);
        
        dfs(candidate);
        for(int i =0;i<V;i++)
        if(!vis[i])
        return -1;
        return candidate;
    }
};

 