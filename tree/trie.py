# -*- coding: utf-8 -*-

"""
性质:

（1）根节点不包含字符，除根节点外的每个节点只包含一个字符。
（2）从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串。
（3）每个节点的所有子节点包含的字符串不相同。

应用
（1）词频统计
（2）比直接用hash节省空间
（3）搜索提示

"""
class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.end = False
        self.counter = 1  # 统计词频

class Trie(object):
    def __init__(self):
        self.root = TrieNode('*')

    def add(self, word):
        node = self.root
        for char in word:
            flag = False # is new node
            for child in node.children:
                if child.char == char:
                    flag = True
                    child.counter += 1
                    node = child
                    break
            if not flag:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node

        node.end = True

    def find(self, word):
        node = self.root
        if len(node.children) == 0:
            return False, 0
        for char in word:
            flag = False # notfound
            for child in node.children:
                if child.char == char:
                    flag = True
                    node = child
                    break
            if not flag:
                return None, 0
        return True, node.counter

if __name__ == '__main__':
    t = Trie()
    t.add('hello')
    t.add('hello')
    t.add('hack')
    t.add('ball')
    t.add('back')
    
    # find
    print(t.find('hello'))
