# -*- coding: utf-8 -*-

"""题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的 min 函数。
"""

class Solution:
    def __init__(self):
        self.items = []

    def push(self, node):
        # write code here
        self.items.append(node)

    def pop(self):
        # write code here
        return self.items.pop()
 
    def top(self):
        # write code here
        return self.items[-1]

    def min(self):
        # write code here
        nitems = sorted(self.items, key=lambda x: x)
        return nitems[0]
       
