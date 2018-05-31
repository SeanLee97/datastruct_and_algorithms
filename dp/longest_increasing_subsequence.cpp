#include <iostream>
using namespace std;
/**
 * 给定一个数列，求的最长递增子序列的长度
 */

int maximum = 0;

// 递归版本
int _recursive(int *arr, int n){
    if (n <= 1)
        return 1;
    int premax, currmax=1, i;
    for (i=1; i<n; i++){
        premax = recursive(arr, i);
        if (*(arr+i-1) < *(arr+n-1) && premax+1 > currmax){
            currmax = premax+1;
        }
    }         
    maximum = max(maximum, currmax);
    return currmax;
}

// 动态规划版本
int dynamic_programming(int *arr, int n){
    int *dp = new int[n+1];
    int i, j;

    // init
    for (i=1; i<n+1; i++){
        *(dp+i) = 1;
    }
    for (i=1; i<n+1; i++){
        for (j=0; j<i; j++){
            if (*(arr+i) > *(arr+j) && *(dp+j) + 1 > *(dp+i)){
                *(dp+i) = *(dp+j) + 1;
            }
        }
    } 
    int result = 0;
    for (i=0; i<n; i++){
        result = max(result, *(dp+i));
    }
    delete []dp;
    return result;
}

// 递归版本
int recursive(int *arr, int n){
    int res = recursive(arr, n);
    res = maximum;
    maximum = 0;
    return res;
}

int main(void){
    int arr[5] = {5, 2, 11, 2, 20};
    int n = 5;
    cout<<LIS_recursive(arr, n)<<endl;
    cout<<dynamic_programming(arr, n)<<endl;
    return 0;
}


