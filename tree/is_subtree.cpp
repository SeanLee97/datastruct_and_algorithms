#include <iostream>
using namespace std;

struct TreeNode{
    int val;
    TreeNode* left = nullptr;
    TreeNode* right = nullptr;
    TreeNode(int val):val(val){}
};

bool issubtree(TreeNode *p1, TreeNode *p2){
    if (p2 == nullptr)
        return true;
    if (p1 == nullptr)
        return false;
    if (p1->val != p2->val)
        return false;
    return issubtree(p1->left, p2->left) && issubtree(p1->right, p2->right);
}

bool check(TreeNode *p1, TreeNode *p2){
    if (p2 == nullptr || p1 == nullptr)
        return false;
    return issubtree(p1, p2) || check(p1->left, p2) || check(p1->right, p2);
}

int main(void){
    TreeNode *p1 = new TreeNode(1);
    p1->left = new TreeNode(2);
    p1->right = new TreeNode(3);
    p1->left->left = new TreeNode(4);
    p1->left->right = new TreeNode(5);

    TreeNode *p2 = new TreeNode(2);
    p2->left = new TreeNode(4);
    p2->right = new TreeNode(5);

    cout<<check(p1, p2)<<endl;
    return 0;
}
