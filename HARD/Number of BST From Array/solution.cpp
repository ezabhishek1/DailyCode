class Solution {
    static bool cmp(const pair<int,int> a, pair<int,int> b){
        return a.first<b.first;
    }
    
  public:
    vector<int> countBSTs(vector<int>& arr) {
        // Code here
        int n = arr.size();
        int cat[16] = {1,1,2,5,14,42,132,429,1430,4862,16796,58786,208012,742900,2674440,9694845};
        
        vector<pair<int,int>> extra;
        for(int i =0; i<n; i++){
            extra.push_back({arr[i], i});
        }
        sort(extra.begin(), extra.end(), cmp);
    
        vector<int> ans(n);
        for(int i = 0; i<n ;i++){
            int smaller = i;
            int larger = n-i-1;
            
            int pos = extra[i].second;
            ans[pos] = (cat[smaller]*cat[larger]);
        }
        
        return ans;
    }
};