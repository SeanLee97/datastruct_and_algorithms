#include <iostream>
using namespace std;

/**
 * 题目描述
 * 01背包问题
 * 有n件物品和一个容量为W的背包。第i件物品的价值是Vt[i]，容量是Wt[i]，求最大价值
 */

const int N = 3;

// 递归版本
int recursive(int n, int Vt[N], int Wt[N], int W){
    if (0 == n)
        return 0;
    if (Wt[n-1] > W)
        return recursive(n-1, Vt, Wt, W);
    else
        return max(Vt[n-1]+recursive(n-1, Vt, Wt, W-Wt[n-1]), 
                   recursive(n-1, Vt, Wt, W));
}

// 动态规划
int dynamic_programming(int n, int Vt[N], int Wt[N], int W){
    int **dp = new int*[n];
    int i, j;
    for (i=0; i<n; i++){
        *(dp+i) = new int[W+1];
    }
    for (i=1; i<n; i++){
        for (j=1; j<=W; j++){
            if (Wt[i] > j)
                *(*(dp+i)+j) = *(*(dp+i-1)+j);
            else
                *(*(dp+i)+j) = max(Vt[i]+*(*(dp+i-1)+j-Wt[i]), *(*(dp+i-1)+j));
        }
    }

    int result = *(*(dp+n-1)+W);
    // 清理堆空间
    for (i=0; i<n; i++){
        delete[] *(dp+i);
    }
    delete []dp;
    return result;
}

int main(void){
    int Vt[] = {30, 100, 120};
    int Wt[] = {10, 20, 30};
    int W = 50;
    int n = N; 
    int m = recursive(n, Vt, Wt, W);
    cout<<m<<endl;
    m = dynamic_programming(n, Vt, Wt, W);
    cout<<m<<endl;
    return 0;
}


