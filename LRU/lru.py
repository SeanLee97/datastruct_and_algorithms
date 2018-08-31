# -*- coding: utf-8 -*-

"""
Description:
    采用dict来存储，k,v; 采用k来实现LRU算法
"""

class LRUCache(object):
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.key = []
        self.store = {}

    def put(self, k, v):
        if k in self.key:
            self.key.remove(k)            
        elif len(self.store) == self.capacity:
            del self.store[self.key.pop()]

        self.key = [k] + self.key
        self.store[k] = v

    def get(self, k):
        if k in self.store:
            self.key.remove(k)
            self.key = [k] + self.key
            return self.store[k]
        return None

    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, k):
        return self.get(k)

if __name__ == '__main__':
    cache = LRUCache()
    cache.put('a', '1')
    cache.put('b', '2')
    cache.put('c', '3')
    cache.put('d', '4')
    cache['d'] = 5
    print(cache.get('a'))
    print(cache['d'])