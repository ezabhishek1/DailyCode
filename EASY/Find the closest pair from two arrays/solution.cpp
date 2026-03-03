#define ll long long
class Solution {
  public:
    vector<int> findClosestPair(vector<int> &a, vector<int> &b, int x) {
        // code here
        int n=a.size(),m=b.size();
        int i=0,j=m-1,mindiff=INT_MAX;
        vector<int>best;
        while(i<n && j>=0){
            int sum=a[i]+b[j];
            if(mindiff>abs(sum-x)){
                mindiff=abs(sum-x);
                best={a[i],b[j]};
            }
            if(sum>x){
                j--;
            } else if(sum<x){
                i++;
            } else {
                return {a[i],b[j]};
            }
        }
        return best;
    }
};