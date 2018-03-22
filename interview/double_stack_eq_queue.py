# -*- coding: utf-8 -*-

class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, element):
        self.stack1.append(element)
        
    def pop(self):
        while len(self.stack1) > 0:
            t = self.stack1.pop()
            self.stack2.append(t)
        return self.stack2.pop()

queue = Queue()
queue.push(1)
queue.push(2)
print(queue.pop())
print(queue.pop()) 
