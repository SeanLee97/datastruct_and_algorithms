# -*- coding: utf-8 -*-

"""题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""

class Solution:
    def reverse(self, data, start, end):
        if len(data) == 0 or start < 0 or end > len(data):
            return 
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    def LeftRotateString(self, s, n):
        # write code here
        #return s[n:]+s[:n]
        lst = list(s)
        self.reverse(lst, 0, n-1)
        print(lst)
        self.reverse(lst, n, len(lst)-1)
        self.reverse(lst, 0, len(lst)-1)
        return ''.join(lst)

if __name__ == '__main__':
    s = Solution()
    ns = s.LeftRotateString('abcXYZdef', 3)
    print(ns)
