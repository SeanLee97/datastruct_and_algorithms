#include <iostream>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left=nullptr;
    TreeNode *right=nullptr;
    TreeNode(int val):val(val){}
};

int check(TreeNode *pRoot, int m, int n){
    if (pRoot == nullptr){
        return -1;
    }
    if (pRoot->val < m && pRoot->val < n){
        return check(pRoot->right, m, n);
    }
    if (pRoot->val > m && pRoot->val > n){
        return check(pRoot->left, m, n);
    }
    return pRoot->val;

}

int main(void){
    TreeNode *pRoot = new TreeNode(1);
    pRoot->left = new TreeNode(3);
    pRoot->left->left = new TreeNode(2);
    pRoot->left->right = new TreeNode(4);
    pRoot->right = new TreeNode(5);
    cout<<check(pRoot, 4, 5)<<endl;
    return 0;
}
