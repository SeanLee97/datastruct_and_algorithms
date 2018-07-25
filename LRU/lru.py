# -*- coding: utf-8 -*-

"""
Description:
    采用dict来存储，k,v; 采用k来实现LRU算法
"""

class LRUCache(object):
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.store = {}
        self.key = []

    def put(self, k, v):
        if k in self.store:
            self.key.remove(k)
            self.key = [k] + self.key
            self.store[k] = v
        elif len(self.store.keys()) == self.capacity:
            last_key = self.key.pop()
            del self.store[last_key]
            self.key = [k] + self.key
            self.store[k] = v
        else:
            self.store[k] = v
            self.key = [k] + self.key
    def get(self, k):
        if k in self.store:
            self.key.remove(k)
            self.key = [k] + self.key
            return self.store[k]

        return False

if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1, 2)
    cache.put(2, 3)
    cache.put(3, 6)
    print(cache.get(2))
    print(cache.get(1))
