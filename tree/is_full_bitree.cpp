#include <iostream>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left=nullptr;
    TreeNode *right=nullptr;
    TreeNode(int val):val(val){}
};

bool check(TreeNode *pRoot){
    if (pRoot == nullptr){
        return true;
    }
    if (pRoot->left == nullptr && pRoot->right != nullptr){
        return false;
    }
    return check(pRoot->left) && check(pRoot->right);
}

int main(void){
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    cout<<check(root)<<endl;

    return 0;
}
