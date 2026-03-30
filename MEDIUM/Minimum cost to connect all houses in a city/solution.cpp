
class Solution {
  public:
    // This is a greedy algo
    // Keep connecting the houses from minimum to maximum without redundancies
    // Redundancy is for example 1->2->3->4 is there and 5->6 is there
    // Now connecting 3 to 6 
    int findUltimateParent(vector<int>& parent, int node)
    {
        if(parent[node] == node) return node;
        return parent[node] = findUltimateParent(parent, parent[node]);
    }
    void dsu(vector<int>& parent, vector<int>& size, int u, int v)
    {
        int ulp_u = findUltimateParent(parent, u);
        int ulp_v = findUltimateParent(parent, v);
        if(ulp_u == ulp_v) return;
        if(size[ulp_u] < size[ulp_v])
        {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else
        {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
    int minCost(vector<vector<int>>& houses) {
        // code here
        int n = houses.size();
        vector<int> parent(n);
        for(int i = 0; i < n; i++) parent[i] = i;
        vector<int> size(n, 1);
        vector<vector<int>> edges;
        for(int i = 0; i < n; i++)
        {
            for(int j = i+1; j < n; j++)
            {
                int dist = abs(houses[i][0]-houses[j][0]) + abs(houses[i][1]-houses[j][1]);
                edges.push_back({i, j, dist});
            }
        }
        sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b)
        {
            return a[2] < b[2];
        });
        int ans = 0;
        for(vector<int>& i: edges)
        {
            if(findUltimateParent(parent, i[0]) != findUltimateParent(parent, i[1]))
            {
                ans += i[2];
                dsu(parent, size, i[0], i[1]);
            }
        }
        return ans;
    }
};