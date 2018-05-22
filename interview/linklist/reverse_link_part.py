# -*- coding: utf-8 -*-

class LinkNode(object):
    def __init__(self, val, nexT=None):
         self.val = val
         self.nexT = nexT

# loop func
def loop_f(head, n):
    prev = head
    curr = head.nexT
    n = n-1
    while curr and n > 0:
        t = curr.nexT
        curr.nexT = prev
        prev = curr
        curr = t
        n -= 1
    head.nexT = curr
    return prev    

def echo(head):
    while head:
        print(head.val)
        head = head.nexT

ll = LinkNode(1, LinkNode(2, LinkNode(3, LinkNode(4, LinkNode(5)))))

head = loop_f(ll, 3)
echo(head)
