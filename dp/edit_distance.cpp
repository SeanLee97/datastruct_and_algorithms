#include <iostream>
using namespace std;

/**
 * 题目描述
 * 给定两个字符串（源串，目的串），求得源串转化为目的串的最小编辑距离
 */

template<typename T>
T abs(T x){
    return x>0 ? x : 0-x;
}

// 递归版本
int recursive(string str1, string str2, int m, int n){
    if (m == 0 || n == 0)
        return abs(m-n);

    if (str1[m-1] == str2[n-1])
        return recursive(str1, str2, m-1, n-1);
    else
        return 1 + min(min(recursive(str1, str2, m, n-1), 
                     recursive(str1, str2, m-1, n)), 
                     recursive(str1, str2, m-1, n-1));
}

// 动态规划版本
int dynamic_programming(string str1, string str2, int m, int n){
    int **dp = new int*[m];
    int i, j;
    for (i=0; i<m; i++){
        *(dp+i) = new int[n];
    }
    // bottom-up
    for (i=1; i<m; i++){
        for (j=1; j<n; j++){
            if (str1[i] == str2[j]){
                *(*(dp+i)+j) = *(*(dp+i-1)+j-1);
            } else{
                *(*(dp+i)+j) = 1 + min(min(*(*(dp+i-1)+j), *(*(dp+i)+j-1)), *(*(dp+i-1)+j-1));
            }
        }
    }
    return *(*(dp+m-1)+n-1);
}

int main(void){
    string str1 = "peer";
    string str2 = "pair";
    int dist = recursive(str1, str2, str1.length(), str2.length());
    cout<<dist<<endl;
    dist = dynamic_programming(str1, str2, str1.length(), str2.length());
    cout<<dist<<endl;
    return 0;
}

