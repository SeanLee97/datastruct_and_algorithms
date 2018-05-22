# -*- coding: utf-8 -*-

"""题目描述
用两个栈来实现一个队列，完成队列的 Push 和 Pop 操作。
队列中的元素为 int 类型。
"""

class Queue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []
    def push(self, x):
        self.instack.append(x)
    
    def pop(self):
        if len(self.instack) > 0 and len(self.outstack) == 0:
            for _ in range(len(self.instack)):
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    print(q.pop())
    print(q.pop())
