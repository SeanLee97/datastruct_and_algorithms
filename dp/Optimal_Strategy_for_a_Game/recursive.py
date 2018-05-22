# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(lst, begin, end):
    if begin == end:
        return lst[begin]  
    if begin + 1 == end:
        # 如果只有两个数，则选择大数
        return max(lst[begin], lst[end])
    # 如果当前用户选择开始位置的数，那么就下来第二个用户就会从剩余数
    # 开头或结尾中选择较大的数,也就是说当前用户下一个数是
    # f(begin+1, end-1)：即第二个用户选择了末尾的数和 
    # f(begin+2, end)：即第二个用户选择了剩余数开头的数中较小的
    a = lst[begin] + min(f(lst, begin+1, end-1), f(lst, begin+2, end))
    # 如果当前用户选择了结尾的数，则类似
    b = lst[end] + min(f(lst, begin, end-2), f(lst, begin+1, end-1))
    # 最后选择两种选择中较大的
    return max(a, b)

lst = [3, 9, 1, 2]
print(f(lst, 0, len(lst)-1))
