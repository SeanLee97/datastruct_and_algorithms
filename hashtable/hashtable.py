# -*- coding: utf-8 -*-

"""Implement hashtable
"""

# 开放定址法哈希
class HashTable(object):
    def __init__(self, capacity=1000, skip=2):
        self.capacity = capacity
        self.skip = skip
        self.entry = [None] * self.capacity # key
        self.data = [None] * self.capacity

    def _hash(self, key):
        if isinstance(key, str):
            key = hash(key)
        return key % self.capacity

    def _rehash(self, key):
        if isinstance(key, str):
            key = hash(key)
        return (key + self.skip) % self.capacity

    def put(self, key, val):
        hashk = self._hash(key)
        if self.entry[hashk] == None:
            self.entry[hashk] = key
            self.data[hashk] = val
        elif self.entry[hashk] == key:
            # update
            self.data[hashk] = val
        else:
            # collision
            cntk = self._rehash(key)
            while self.entry[cntk] != None and self.entry[cntk] != key:
                cntk = self._rehash(cntk)
                self.data[cntk] = val
            self.entry[cntk] = key

    def get(self, key):
        hashk = self._hash(key)
        data = None
        cntk = hashk
        while self.entry[cntk] != None:
            if self.entry[cntk] == key:
                return self.data[cntk]
            cntk = self._rehash(cntk)
            if cntk == hashk:
                break
        return data

    def getall(self):
        for k in self.entry:
            if k != None:
                yield k, self.data[k]

# 链地址法哈希
class HashTableLink(object):
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.entry = [None] * self.capacity
        
    def _hash(self, key):
        if isinstance(key, str):
            key = hash(key)
        return key % self.capacity

    def put(self, key, val):
        hashk = self._hash(key)
        if self.entry[hashk] == None:
            self.entry[hashk] = [(key, val)]
        else:
            self.entry[hashk] = [(key, val)] + self.entry[hashk]

    def get(self, key):
        hashk = self._hash(key)
        links = self.entry[hashk]
        for item in links:
            if item[0] == key:
                return item[1]
        return None

    def getall(self):
        for links in self.entry:
            if links == None:
                continue
            for item in links:
                yield item[0], item[1]    
        
        
        
