#pragma GCC diagnostic error "-std=c++11"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct TreeNode{
    int val;
    TreeNode *left=nullptr;
    TreeNode *right=nullptr;
    TreeNode(int val):val(val){}
};

class Solution{
    public:
        vector<vector<int> > buffer;
        void find_path(TreeNode *p, int tot, int target, vector<int> tmp);
        vector<vector<int> > FindPath(TreeNode *p, int target);
};

void Solution::find_path(TreeNode *p, int tot, int target, vector<int> tmp){
    if (p == nullptr)
        return;

    tot += p->val;
    tmp.push_back(p->val);
    if (tot==target){
        buffer.push_back(tmp);
    }
    find_path(p->left, tot, target, tmp);
    find_path(p->right, tot, target, tmp);
    tmp.pop_back();
}

vector<vector<int>> Solution::FindPath(TreeNode *p, int target){
    if (p == nullptr)
        return buffer;
    vector<int> tmp;
    find_path(p, 0, target, tmp);
    return buffer;
}

int main(void){
    TreeNode *p = new TreeNode(1);
    p->left = new TreeNode(2);
    p->right = new TreeNode(3);
    Solution *s = new Solution();
    vector<vector<int> >res = s->FindPath(p, 3);
    for (vector<int> lst : res){
        for_each(lst.begin(), lst.end(), [](int &x){cout<<x<<" ";});
        cout<<endl;
    }
    return 0;
}