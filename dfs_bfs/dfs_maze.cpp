#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

class Solution{
    public:
        int minimum = INT_MAX;
        vector<vector<int>>matrix;
        vector<vector<int>>pos{{-1,0}, {0, 1}, {1, 0}, {0, -1}};
        void dfs(int m, int n, int i, int j, int step, vector<vector<bool>>visit);
        int find(vector<vector<int>>matrix);
};

void Solution::dfs(int m, int n, int i, int j, int step, vector<vector<bool>>visit){
    if (i < 0 || i > m || j < 0 || j > n || visit[i][j] || matrix[i][j] == 1){
        return;
    }
    //cout<<i<<","<<j<<" "<<m<<","<<n<<" "<<step<<endl;
    if (i == m && j == n){
        minimum = min(minimum, step);
        return;
    }
    visit[i][j] = true;
    for (int k=0; k<pos.size(); k++){
        dfs(m, n, i+pos[k][0], j+pos[k][1], step+1, visit);
    }
}

int Solution::find(vector<vector<int>>mat){
    matrix = mat;
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<bool>>visit;
    for (int i=0; i<m; i++){
        vector<bool>tmp;
        for (int j=0; j<n; j++){
            tmp.push_back(false);
        }
        visit.push_back(tmp);
    }
    dfs(m-1, n-1, 0, 0, 0, visit);
    return minimum;
}
int main(void){
    vector<vector<int>> maze = {
        {0, 1, 0, 0, 0},
        {0, 0, 0, 1, 0},
        {0, 0, 0, 0, 0},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 1, 0}
    };
    Solution s;
    int step = s.find(maze);
    cout<<"Minimum step: "<<step<<endl;
    return 0;
}
