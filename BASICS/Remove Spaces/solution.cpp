class Solution {
  public:
    virtual string dfs(int i, string &s){
      if(i==s.size()) return "";
      string temp="";
      
      if(s[i] != ' ') temp+=s[i];
      
      return temp+dfs(i+1, s);
    }
    virtual string removeSpaces(string& s){
      return dfs(0, s);
    }
};

