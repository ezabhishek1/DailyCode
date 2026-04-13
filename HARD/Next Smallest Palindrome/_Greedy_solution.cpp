class Solution {
  public:
    vector<int> nextPalindrome(vector<int>& num) {
        // code here
        int n=num.size();
        bool is9 = true;
        for(auto& x:num){
            if(x!=9){
                is9 = false;
            }
        }
        if(is9){
            vector<int> res(n+1, 0);
            res[0]=1;
            res[n]=1;
            return res;
        }
        
        vector<int> ans = num;
        int l=0; 
        int r=n-1;
        int mid = l+(r-l)/2;
        if(n%2!=0){ //odd
            l = mid-1;
            r = mid+1;
            bool inc = false;
            bool same = false;
            while(r<n && l>=0){
                if(num[l]>num[r]){
                    inc = true;
                    break;
                }
                else if(num[l]<num[r]){
                    inc = false;
                    break;
                }
                else{
                    r++;
                    l--;
                }
            }
            if(r==n){
                same = true;
            }
            
            l=0;
            r=n-1;
            while(l<mid){
                ans[r] = ans[l];
                r--;
                l++;
            }
            
            l=mid;
            r=mid;
            if(!inc || same){
                if(ans[mid]==9){
                    while(l>=0 && r<n && ans[l]==9 && ans[r]==9){
                        ans[l]=0;
                        ans[r]=0;
                        l--;
                        r++;
                    }
                    if(l>=0 && r<n){
                        ans[l]++;
                        ans[r]++;
                    }
                }
                else{
                    ans[mid]++;
                    return ans;
                }
            }
        }
        else{
            // mid = mid-1;
            l=mid-1;
            r=mid+2;
            bool inc = false;
            bool same = false;
            while(l>=0 && r<n){
                if(num[l]>num[r]){
                    inc = true;
                    break;
                }
                else if(num[l]<num[r]){
                    inc = false;
                    break;
                }
                else{
                    r++;
                    l--;
                }
            }
            if(r==n){
                same = true;
            }
            
            l=0;
            r=n-1;
            while(l<mid){
                ans[r] = ans[l];
                r--;
                l++;
            }
            
            l=mid;
            r=mid+1;
            if(ans[mid]!=ans[mid+1]){
                if(ans[mid]>ans[mid+1]){
                    ans[mid+1] = ans[mid];
                }
                else{
                    ans[mid]++;
                    ans[mid+1]=ans[mid];
                }
                return ans;
            }
            else if(!inc || same){
                if(ans[mid]==9){
                    while(l>=0 && r<n && ans[l]==9 && ans[r]==9){
                        ans[l]=0;
                        ans[r]=0;
                        l--;
                        r++;
                    }
                    if(l>=0 && r<n){
                        ans[l]++;
                        ans[r]++;
                    }
                }
                else{
                    ans[mid]++;
                    ans[mid+1]++;
                    return ans;
                }
            }
        }
        
        
        return ans;
    }
};