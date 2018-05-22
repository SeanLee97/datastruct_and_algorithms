# -*- coding: utf-8 -*-

"""题目描述
栈的压入、弹出序列,
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列 1,2,3,4,5 是某栈的压入顺序，序列 4,5,3,2,1 是该压栈序列对应的一个弹出序列，但 4,3,5,1,2 就不可能是该压栈序列的弹出序列。
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        self.stack = []
        l = len(pushV)
        popidx = 0
        for i in range(l):
            self.stack.append(pushV[i])
            while popidx < l and popV[popidx] == self.stack[-1]:
                self.stack.pop()
                popidx += 1
        return True if len(self.stack) == 0 else False
