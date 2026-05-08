class Solution {
  public:

    bool isValid(string s) {

        int count = 0;

        for(char ch : s) {

            if(ch == '(') {
                count++;
            }
            else if(ch == ')') {

                count--;

                if(count < 0) {
                    return false;
                }
            }
        }

        return count == 0;
    }

    vector<string> validParenthesis(string s) {

        vector<string> ans;

        unordered_set<string> visited;

        queue<string> q;

        q.push(s);
        visited.insert(s);

        bool found = false;

        while(!q.empty()) {

            int size = q.size();

            for(int z = 0; z < size; z++) {

                string curr = q.front();
                q.pop();

                if(isValid(curr)) {

                    ans.push_back(curr);
                    found = true;
                }

                // minimum level reached
                if(found) {
                    continue;
                }

                for(int i = 0; i < curr.size(); i++) {

                    if(curr[i] != '(' && curr[i] != ')') {
                        continue;
                    }

                    string next =
                        curr.substr(0, i) +
                        curr.substr(i + 1);

                    if(!visited.count(next)) {

                        visited.insert(next);
                        q.push(next);
                    }
                }
            }

            // stop after current level
            if(found) {
                break;
            }
        }

        return ans;
    }
};