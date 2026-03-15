class Solution {
public:
    unordered_map<int,int> mpp;

    int dfs(Node* root, int curr, int k) {
        if (!root) return 0;

        curr += root->data;
        int total = mpp[curr - k];

        mpp[curr]++;
        total += dfs(root->left, curr, k);
        total += dfs(root->right, curr, k);

        if (--mpp[curr] == 0)
            mpp.erase(curr);

        return total;
    }

    int countAllPaths(Node* root, int k) {
        mpp.clear();
        mpp[0] = 1;
        return dfs(root, 0, k);
    }
};