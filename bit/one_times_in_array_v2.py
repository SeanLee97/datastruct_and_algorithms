# -*- coding: utf-8 -*-

# 题目描述:
# 在一个数组中除了两个数字只出现1次外，其他均出现2次，求这两个数字
# 思路：
"""
设题目中这两个只出现1次的数字分别为A和B，如果能将A，B分开到二个数组中，
那显然符合“异或”解法的关键点了。
因此这个题目的关键点就是将A，B分开到二个数组中。
由于A，B肯定是不相等的，因此在二进制上必定有一位是不同的。
根据这一位是0还是1可以将A，B分开到A组和B组。
而这个数组中其它数字要么就属于A组，要么就属于B组。
再对A组和B组分别执行“异或”解法就可以得到A，B了。
而要判断A，B在哪一位上不相同，只要根据A异或B的结果就可以知道了，
这个结果在二进制上为1的位都说明A，B在这一位上是不相同的。
https://blog.csdn.net/morewindows/article/details/8214003
"""
def solution(lst):
    # 1. 先找出lst异或的结果
    tmp = 0
    for v in lst:
        tmp ^= v
    #print(tmp)

    # 从左边数找到第一个为1的位
    j = 0
    while j<32:
        if ((tmp>>j) & 1) == 1:
            break
        j+=1
    # 第j位为1，说明这两个数字在j位上是不相同的，由此分组
    lst1 = []
    lst2 = []
    for v in lst:
        if (v>>j) & 1 == 1:
            lst1.append(v)
        else:
            lst2.append(v)
    x = 0
    y = 0
    for v in lst1:
        x ^= v
    for v in lst2:
        y ^= v
    return x, y

if __name__ == '__main__':
    print(solution([1, 1, 3, 5, 2, 2]))
