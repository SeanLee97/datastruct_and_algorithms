# -*- coding: utf-8 -*-

"""题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为 We Are Happy. 则经过替换之后的字符串为 We%20Are%20Happy。
"""

# 转化成数组实现
def solution(string):
    n = len(string)-1
    string = list(string)
    while n >= 0:
        if string[n] == ' ':
            string[n] = '%20'
        n -= 1
    return ''.join(string)

if __name__ == '__main__':
    s = 'We Are Happy.'
    t = solution(s)
    print('raw: ', s)
    print('replaced: ', t)
