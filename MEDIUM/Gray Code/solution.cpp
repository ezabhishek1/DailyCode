class Solution {
  public:
    vector<string> graycode(int n) {
        vector<string> result;
        
        int total = 1 << n;
        
        for (int i = 0; i < total; i++) {
            
            int gray = i ^ (i >> 1);
            
            string binary = "";
            
            for (int bit = n - 1; bit >= 0; bit--) {
                if (gray & (1 << bit))
                    binary += '1';
                else
                    binary += '0';
            }
            
            result.push_back(binary);
        }
        
        return result;
    }
};