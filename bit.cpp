#include <iostream>
using namespace std;

int get_bit(int num, int pos){
    if (pos > 32){
        return -1;
    }
    return num & (1<<pos);
}

int set_bit(int num, int pos){
    if (pos > 32){
        return -1;
    }
    return num | (1<<pos);
}

int clear_bit(int num, int pos){
    if (pos > 32)
        return -1;
    return num & (~(1<<pos));
}

// 判断奇偶
bool is_odd(int num){
    return num & 1;
}

// 交换两数(仅支持整数)
void swap(int &x, int &y){
    x ^= y;
    y ^= x;
    x ^= y;
}

// 变换符号(正变负，负变正)
int change_sign(int num){
    return ~num + 1;
}

// 求绝对值
int abs(int num){
    int i = num >> 31;   //结果可能为 0(0x0000...0000) 或 -1(0x1111...1111)
    //return i == 0 ? num : (~num + 1);

    // x ^ 0x0000...0000 = x
    // x ^ 0x1111...1111 = ~x
    // 当 i = 0  --> num ^ i = num  --> (num ^ i) - i = num
    // 当 i = -1 --> num ^ i = ~num --> (num ^ i) -i = ~num + 1 = -num
    return ((num ^ i) - i);// 不用三元运算
}

int main(void){
    cout<<get_bit(5, 2)<<endl;  // 4
    cout<<set_bit(1, 1)<<endl;  // 3
    cout<<clear_bit(5, 2)<<endl;// 1

    if (is_odd(1)){
        cout<<"1 is odd"<<endl;
    }

    int x = 1, y = 2;
    swap(x, y);
    cout<<x<<", "<<y<<endl;
    cout<<change_sign(1)<<endl;
    cout<<change_sign(-3)<<endl;
    return 0;
}
