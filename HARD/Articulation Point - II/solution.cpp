#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> articulationPoints(int V, vector<vector<int>>& edges) {
        
        // Step 1: Build adjacency list
        vector<vector<int>> adj(V);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        vector<int> tin(V, -1), low(V, -1);
        vector<bool> visited(V, false);
        vector<bool> isArt(V, false);

        int timer = 0;

        // DFS function
        function<void(int, int)> dfs = [&](int node, int parent) {
            visited[node] = true;
            tin[node] = low[node] = timer++;
            int children = 0;

            for (auto it : adj[node]) {
                if (it == parent) continue;

                if (!visited[it]) {
                    dfs(it, node);

                    // update low
                    low[node] = min(low[node], low[it]);

                    // check articulation condition
                    if (low[it] >= tin[node] && parent != -1) {
                        isArt[node] = true;
                    }

                    children++;
                } else {
                    // back edge
                    low[node] = min(low[node], tin[it]);
                }
            }

            // root case
            if (parent == -1 && children > 1) {
                isArt[node] = true;
            }
        };

        // Run DFS for all components
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, -1);
            }
        }

        // Collect answer
        vector<int> result;
        for (int i = 0; i < V; i++) {
            if (isArt[i]) result.push_back(i);
        }

        if (result.empty()) return {-1};
        return result;
    }
};
