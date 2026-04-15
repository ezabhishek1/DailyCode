class Solution {
    int cntSpace(const string& s){
        int cnt=0;
        for(char c : s){
            if(c==' ')cnt++;
        }
        return cnt;
    }
  public:
    string URLify(string &s) {
        // code here
        int len=s.length();
        int spaces=cntSpace(s);
        if(spaces==0)return s;
        int newLen=len+2*spaces;
        s.resize(newLen);
        int i=len-1;
        int j=newLen-1;
        while(i>=0){
            if(s[i]==' '){
                s[j--]='0';
                s[j--]='2';
                s[j--]='%';
            }else{
                s[j--]=s[i];
            }
            i--;
        }
        return s;
    }
};