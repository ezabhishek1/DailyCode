class Solution {
  public:
    vector<string>ans;
    bool isValid(string &str){
        if(str.size()>1 && str[0]=='0')return false;
        int val=stoi(str);
        return val<256;
    }
    void dfs(string &s,int idx,int parts,string curr){
        if(idx>=s.size() && parts==4){
            curr.pop_back();
            ans.push_back(curr);
            return;
        }
        if(parts>=4)return;
        
        for(int len=1;len<=3;len++){
            int j=idx+len;
            if(j>s.size())break;
            
            string seg=s.substr(idx,len);
            if(isValid(seg)){
                dfs(s,j,parts+1,curr+seg+".");
            }
        }
    }
    vector<string> generateIp(string &s) {
        // code here
        dfs(s,0,0,"");
        return ans;
    }
};