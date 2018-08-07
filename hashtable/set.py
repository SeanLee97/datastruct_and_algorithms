# -*- coding: utf-8 -*-

from hashtable import HashTable, HashTableLink

#class Set(HashTable):
class Set(HashTableLink):
    def __init__(self):
        super(Set, self).__init__()

    def add(self, v):
        self.put(v, v)

    def __contains__(self, v):
        return self.get(v) == v

    def _all(self):
        lst = []
        [lst.append(v) for k, v in self.getall()]
        return lst

    def __iter__(self):
        return self._all()

    def __call__(self):
        return self._all()

    def __str__(self):
        return str(self._all())

if __name__ == '__main__':
    s = Set() 
    s.add(12)
    s.add(12)
    s.add(2)
    print(s)
     
