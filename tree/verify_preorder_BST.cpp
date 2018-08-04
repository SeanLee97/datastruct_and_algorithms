#include <iostream>
#include <vector>
#include <stack>
#include <limits.h>
using namespace std;

bool check(vector<int> lst){
    int root = INT_MIN;
    stack<int>S;
    for (int v : lst){
        if (v < root){
            return false;
        }
        while (S.size() > 0 && S.top() < v){
            root = S.top();
            S.pop();
        }
        S.push(v);
    }
    return true;
}

int main(void){
    vector<int>lst{4, 2, 1, 3, 5};
    cout<<check(lst)<<endl;
    return 0;
}
