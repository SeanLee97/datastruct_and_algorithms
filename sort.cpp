#include <iostream>
#include <cstdlib>
#define LEN(arr) sizeof(arr)/sizeof(arr[0])
using namespace std;

/**
 * c++实现常用排序算法
 * 冒泡排序、插入排序、选择排序、快速排序、堆排、归并排序
 */

void swap(int *arr, int i, int j){
    int t;
    t = *(arr+j);
    *(arr+j) = *(arr+i);
    *(arr+i) = t;
}

// bubble sort
void bubble_sort(int *arr, int n){
    int i, j; 
    for (i=0; i<n; i++){
        for (j=i; j<n; j++){
            if (*(arr+j) < *(arr+i)){
                swap(arr, i, j);
            }
        }
    }
}

// insert sort
void insert_sort(int *arr, int n){
    int i, j, k;
    for (i=1; i<n; i++){
        j = i-1;
        k = *(arr+i);
        while (j>=0 && k < *(arr+j)){
            *(arr+j+1) = *(arr+j);
            j--;
        }
        *(arr+j+1) = k;
    }
}

// select sort
void select_sort(int *arr, int n){
    int i, j, minimum, min_idx;
    for (i=0; i<n; i++){
        minimum = *(arr+i);
        min_idx = i;
        for (j=i+1; j<n; j++){
            if (*(arr+j) < minimum){
                minimum = *(arr+j);
                min_idx = j;
            }
        }
        // swap
        swap(arr, i, min_idx);
    }
}

// 快排
int partition(int *arr, int low, int high){
    //  选择随机数作为哨兵
    int randint = rand()%high + low;
    swap(arr, randint, high);
    
    int store_idx=low, i, j, privot= *(arr+high);
    for (i=low; i<high; i++){
        if (*(arr+i) < privot){
            swap(arr, i, store_idx);
            store_idx++;
        }
    }
    swap(arr, store_idx, high);
    return store_idx;
}

int quick_sort(int *arr, int low, int high){
    if (low < high){
        int mid = partition(arr, low, high);
        quick_sort(arr, low, mid-1);
        quick_sort(arr, mid+1, high);
    }
}

// 堆排
// 构建大顶堆
void build_maxheap(int *arr, int root, int n){
    int L, R, largest;
    L = 2*root+1;
    R = 2*root+2;
    largest = root;
    if (L < n && *(arr+L) > *(arr+largest)){
        largest = L;
    }
    if (R < n && *(arr+R) > *(arr+largest)){
        largest = R;
    }

    if (largest != root){
        swap(arr, largest, root);
        build_maxheap(arr, largest, n);
    }
}

void heap_sort(int *arr, int n){
    int i;
    for (i=n-1; i>=0; i--){
        // 构建初始大顶堆
        build_maxheap(arr, i, n);
    }
    for (i=n-1; i>=0; i--){
        build_maxheap(arr, 0, i);
        swap(arr, 0, i);
    }
}

// 归并排序
void merge(int *arr, int low, int mid, int high){
    int n1, n2, i, j, k;
    n1 = mid - low + 1;
    n2 = high - mid;
    int *L = new int[n1];
    int *R = new int[n2];
    for (i=0; i<n1; i++){
        *(L+i) = *(arr+low+i);
    }
    for (j=0; j<n2; j++){
        *(R+j) = *(arr+mid+j+1);
    }
    k = low;
    i = 0;
    j = 0;
    while (i<n1 && j<n2){
        if (*(L+i) < *(R+j)){
            *(arr+k) = *(L+i);
            i++;
        }else{
            *(arr+k) = *(R+j);
            j++;
        }
        k++;
    }
    while (i<n1){
        *(arr+k) = *(L+i);
        i++;
        k++;
    }
    while (j<n2){
        *(arr+k) = *(R+j);
        j++;
        k++;
    }
}

void merge_sort(int *arr, int low, int high){
    if (low < high){
        int mid = (low+high) / 2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}

// 输出
void echo(int *arr, int n){
    for (int i=0; i<n; i++){
        cout<< *(arr+i) <<" ";
    }
    cout<<endl;
}

int main(void){
    int arr[] = {2, 1, 4, 3};
    int n = LEN(arr);
    int *lst;
    
    cout<<"原始数组"<<endl;
    echo(arr, n);
    
    cout<<"冒泡"<<endl;
    lst = arr;
    bubble_sort(lst, n);
    echo(lst, n);
    
    cout<<"插入"<<endl;
    lst = arr;
    insert_sort(lst, n);
    echo(lst, n);
     
    cout<<"选择"<<endl;
    lst = arr;
    select_sort(lst, n);
    echo(lst, n);

    cout<<"快排"<<endl;
    lst = arr;
    quick_sort(lst, 0, n-1);
    echo(lst, n);

    cout<<"堆排"<<endl;
    lst = arr;
    heap_sort(lst, n);
    echo(lst, n);
    
    cout<<"归并"<<endl;
    lst = arr;
    merge_sort(lst, 0, n-1);
    echo(lst, n);
    
    return 0;
}
