#include <iostream>
#include <vector>
#include <algorithm>

/*
 * Given a set of distinct integers, S, return all possible subsets.
 * Note: Elements in a subset must be in non-descending order. The solution set m
 * For example, If S = [1,2,3], a solution is: [ [3], [1], [2], [1,2,3], [1,3], [
 * 子集问题
 */

using namespace std;

class Solution{
    public:
        vector<vector<int>> res;
        void dfs(vector<int>lst, int n, vector<int> tmp, vector<bool> visit);
        vector<vector<int>> get_subset(vector<int> lst);
};

void Solution::dfs(vector<int>lst, int n, vector<int>tmp, vector<bool>visit){
    res.push_back(tmp);

    for(int i=0; i<n; i++){
        if(! visit[i]){
            tmp.push_back(lst[i]);
            visit[i] = true;
            dfs(lst, n, tmp, visit);
            visit[i] = false;
            tmp.pop_back();
        }
    }
}

vector<vector<int>> Solution::get_subset(vector<int>lst){
    int n = lst.size();
    vector<bool>visit;
    for (int i=0; i<n; i++){
        visit.push_back(false);
    }
    vector<int> tmp;
    dfs(lst, n, tmp, visit);

    return res;
}

int main(void){
    vector<int>lst {1, 2, 3};
    Solution s;
    vector<vector<int>> res = s.get_subset(lst);

    for(vector<int> p : res){
        for_each(p.begin(), p.end(), [](int &x){cout<<x<<" ";});
        cout<<endl;
    }
    return 0;
}
