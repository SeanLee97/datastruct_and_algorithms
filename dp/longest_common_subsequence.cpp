#include <iostream>
using namespace std;

/**
 * 有两个序列str1、str2，求出两个序列最长公共子序列长度（不要求连续,但要按照顺序）
 */

// 递归版本
int recursive(string str1, string str2, int m, int n){
    if (m == 0 or n == 0)
        return 0;
    if (str1[m-1] == str2[n-1])
        return 1+recursive(str1, str2, m-1, n-1);
    else
        return max(recursive(str1, str2, m-1, n), 
                     recursive(str1, str2, m, n-1));
}

// 动态规划版本
int dynamic_programming(string str1, string str2, int m, int n){
    int **dp = new int*[m+1];
    int i, j;
    for (i=0; i<m+1; i++){
        *(dp+i) = new int[n+1];
    }
 
    for (i=1; i<m+1; i++){
        for (j=1; j<n+1; j++){
            if (str1[i-1] == str2[j-1])
                *(*(dp+i)+j) = 1 + *(*(dp+i-1)+j-1);
            else
                *(*(dp+i)+j) = max(*(*(dp+i-1)+j), *(*(dp+i)+j-1));
        }
    }

    int result = *(*(dp+m)+n);
    // 清理分配的堆空间
    for (i=0; i<m; i++)
        delete[] *(dp+i);
    delete []dp;    

    return result;
}

int main(void){
    string str1 = "ABCDGH";
    string str2 = "AEDFHRB";
    int res;
    //res = recursive(str1, str2, str1.length(), str2.length());
    //cout<<res<<endl;
     
    res = dynamic_programming(str1, str2, str1.length(), str2.length());
    cout<<res<<endl;
    return 0;
}
