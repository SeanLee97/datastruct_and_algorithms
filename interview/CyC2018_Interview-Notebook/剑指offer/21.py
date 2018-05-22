# -*- coding: utf-8 -*-

"""题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

def f(lst):
    l1 = []
    l2 = []
    for x in lst:
        if x & 1 == 1:
            # 奇数
            l1.append(x)
        else:
            l2.append(x)
    return l1 + l2

if __name__ == '__main__':
    print(f([2, 3, 4, 6, 1, 5]))
