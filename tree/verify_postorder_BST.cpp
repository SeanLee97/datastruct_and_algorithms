#include <iostream>
#include <vector>
using namespace std;

bool check(vector<int>lst, int L, int R){
    if (L >= R){
        return true;
    }
    int idx = L;
    while (idx < R - 1 && lst[idx] < lst[R]){
        idx++;
    }
    while (idx < R - 1 && lst[idx] > lst[R]){
        idx++;
    }

    if (idx + 1 != R){
        return false;
    }
    return check(lst, L, idx-1) &&  check(lst, idx, R-1);
}

bool verify(vector<int>lst){
    int len = lst.size();
    if (len == 0){
        return true;
    }
    return check(lst, 0, len-1);
}

int main(void){
    vector<int>lst{1, 3, 2, 5, 4};
    cout<<verify(lst)<<endl;
    return 0;
}
