# -*- coding: utf-8 -*-

"""定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
"""

class Solution:
    def __init__(self):
        self.items = []
        self.min_stack = []  # save min_stack

    def push(self, v):
        self.items.append(v)
        if v < self.top(self.min_stack):
            self.min_stack.append(v)

    def pop(self):
        if len(self.items) > 0:
            v = self.items.pop()
            if v == self.top(self.min_stack):
                self.min_stack.pop()

    def top(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return float('inf')

    def min(self):
        if len(self.min_stack) > 0:
            return self.top(self.min_stack)
        return -1