# -*- coding: utf-8 -*-

"""找零钱问题
假设1元、2元、5元、10元、20元、50元、100元的纸币。现在要用这些钱来支付K元，至少要用多少张纸币？

解析：
用贪心算法的思想，很显然，每一步尽可能用面值大的纸币即可。在日常生活中我们自然而然也是这么做的。在程序中已经事先将Value按照从大到小的顺序排好，第一次我们先取面值最大的，然后取次大的。。。。。。每次取都是从面额最大的开始取，获得局部最优解，而最终获得全局最优解
"""

def solution(lst, k):
    lst = sorted(lst, key=lambda x: -x)
    i = 0
    left = k
    res = []
    while left > 0:
        if left < lst[i]:
            # 当前面值>剩余钱数不取，取下一面值更小的
            i += 1
        else:
            res.append(lst[i])
            left -= lst[i]
    return res

if __name__ == "__main__":
    lst = [50,20,10,5,1]
    k = 96
    print(solution(lst, k))


