# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def LCA(root, m, n):
    if root == None:
        return None
    # 若当前结点的值小于m, n那么说明公共结点在当前结点的右子树
    if root.data < m and root.data < n:
        return LCA(root.right, m, n)
    # 若当前结点的值大于m, n那么说明公共结点在当前结点的左子树
    if root.data > m  and root.data > n:
        return LCA(root.left, m, n)
    # 若两结点有一个为当前结点则当前结点为公共结点，或者当前结点的值大于其中一个值小于其中一个值则当前结点也作为公共结点
    return root.data

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(LCA(root, 10, 14))


    
