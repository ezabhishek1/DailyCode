
/* BST Node
class Node
{
   public:
    int data;
    Node *left;
    Node *right;

    Node(int x){
        data = x;
        left = NULL;
        right = NULL;
    }
}; */

class Solution {
  public:
    vector<Node*> findPreSuc(Node* root, int key) {
        // code here
        Node *tmp1 = root, *tmp2 = root;
        Node *ans1 = NULL, *ans2 = NULL;
        while(tmp1 != NULL) {
            if(tmp1 -> data >= key) {
                tmp1 = tmp1 -> left;
            } else {
                ans1 = tmp1;
                tmp1 = tmp1 -> right;
            }
        }
        while(tmp2 != NULL) {
            if(tmp2 -> data <= key) {
                tmp2 = tmp2 -> right;
            } else {
                ans2 = tmp2;
                tmp2 = tmp2 -> left;
            }
        }
        return {ans1, ans2};
    }
};