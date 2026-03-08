class Solution {
  public:
    bool pythagoreanTriplet(vector<int>& arr) {
        // code here
        unordered_set<int>st(arr.begin(), arr.end());
        int n=arr.size();
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                int a=arr[i];
                int b=arr[j];
                int sq=(a*a)+(b*b);
                int c=sqrt(sq);
                if(c*c==sq && st.find(c)!=st.end()) return 1;
            }
        }
        return 0;
    }
};