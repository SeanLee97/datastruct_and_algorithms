#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
 * 求集合的全排列
 */

class Solution{
    public:
        vector<vector<int>>res;
        void dfs(vector<int>lst, int n, vector<int>tmp, vector<bool>visit);
        vector<vector<int>>get_result(vector<int>);
};

void Solution::dfs(vector<int>lst, int n, vector<int>tmp, vector<bool>visit){
    if (tmp.size() == n){
        res.push_back(tmp);
        return;
    }

    for (int i=0; i<n; i++){
        if (!visit[i]){
            tmp.push_back(lst[i]);
            visit[i] = true;
            dfs(lst, n, tmp, visit);
            visit[i] = false;
            tmp.pop_back();
        }
    }
}

vector<vector<int>> Solution::get_result(vector<int>lst){
    int n = lst.size();
    vector<bool>visit;
    for (int i=0; i<n; i++){
        visit.push_back(false);
    }
    vector<int>tmp;
    dfs(lst, n, tmp, visit);
    return res;
}
int main(void){
    vector<int>lst {1, 2, 3};
    Solution s;
    vector<vector<int>>res = s.get_result(lst);

    for(auto p: res){
        for_each(p.begin(), p.end(), [](int x){cout<<x<<" ";});
        cout<<endl;
    }
    return 0;
}
