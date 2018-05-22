# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Attention: the code only support python3.

from typing import Tuple

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.finished = False
        self.counter = 1

class Trie(object):
    def __init__(self):
        super(Trie, self).__init__()
        self.root = TrieNode('*')
    
    def add(self, word: str):
        node = self.root
        for char in word:
            char_exists = False
            for child in node.children:
                if child.char == char:
                    char_exists = True
                    child.counter += 1
                    node = child
                    break
            if not char_exists:
                n_node = TrieNode(char)
                node.children.append(n_node)
                node = n_node
        node.finished = True

    def find(self, prefix: str) -> Tuple[bool, int]:
        node = self.root
        if not node.children:
            return False, 0
        for char in prefix:
            not_found = True
            for child in node.children:
                if child.char == char:
                    not_found = False
                    node = child
                    break
            if not_found: 
                return False, 0
        return True, node.counter

if __name__ == '__main__':
    t = Trie()
    t.add('hello')
    t.add('helloworld')
    t.add('hack')
    t.add('ball')
    t.add('back')
    
    # find
    print(t.find('back'))
