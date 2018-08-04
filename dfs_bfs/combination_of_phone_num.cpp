#include <iostream>
#include <vector>

using namespace std;

class Solution{
    public:
        vector<vector<string>>table {
            {},
            {"a", "b", "c"},
            {"d", "e", "f"},
            {"g", "h", "i"},
            {"j", "k", "l"},
            {"m", "n", "o"},
            {"p", "q", "r", "s"},
            {"t", "u", "v"},
            {"w", "x", "y", "z"}
        };
        vector<string> res;
        void dfs(string s, string tmp);
        vector<string>get_result(string s);
};

void Solution::dfs(string s, string tmp){
    if (s.length() == 0){
        res.push_back(tmp);
        return;
    }

    int k = int(s[0]) - int('0') - 1;
    for (int i=0; i<table[k].size(); i++){
        dfs(s.substr(1), tmp+table[k][i]);
    }
}

vector<string> Solution::get_result(string s){
    string tmp = "";
    dfs(s, tmp);
    return res;
}

int main(void){
    string s = "23";
    Solution so;
    vector<string> res = so.get_result(s);
    cout<<"result: "<<endl;
    for (string p : res){
        cout<<p<<endl;
    }
    return 0;
}
