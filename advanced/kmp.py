# -*- coding: utf-8 -*-

"""
实现KMP实现算法，匹配子串
推荐链接
1. https://www.youtube.com/watch?v=KG44VoDtsAA
2. https://blog.csdn.net/wjy0330/article/details/39589743
"""

# 获取匹配串的next数组
def get_next(s):
    L = len(s)
    next = [-1] + [0]*(L-1)
    k = -1
    j = 0
    while j < L-1:
        if k == -1 or s[j] == s[k]:
            # p[j]表示后缀，p[k]表示前缀
            k += 1
            j += 1
            if s[j] != s[k]:
                next[j] = k
            else:
                next[j] = next[k]
        else:
            k = next[k]
    return next

def kmp_search(src, tgt):
    i = 0
    j = 0
    slen = len(src)
    tlen = len(tgt)
    next = get_next(tgt)
    while i < slen and j < tlen:
        if j == -1 or src[i] == tgt[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == tlen:
        return i-j
    return -1

if __name__ == '__main__':
    t = 'abcdabd'
    #next = get_next(t)
    #print(next)
    pos = kmp_search('abcdabd', 'abd')
    print(pos)

