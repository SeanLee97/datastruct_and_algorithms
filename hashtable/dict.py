# -*- coding: utf-8 -*-

from hashtable import HashTable, HashTableLink

#class Dict(HashTable):
class Dict(HashTableLink):
    def __init__(self):
        super(Dict, self).__init__()

    # 支持 dict[key] = val 设置值
    def __setitem__(self, k, v):
        self.put(k, v)

    # 支持 dict[key] 直接返回值
    def __getitem__(self, k):
        return self.get(k)

    # 支持 key in dict 判断
    def __contains__(self, k):
        if self.get(k) == None:
            return False
        return True        
        

if __name__ == '__main__':
    d = Dict()
    d['age'] = 12
    d['name'] = 'seanlee'
    d[1] = 5
    d[12] = 5
    print(d['age'])
    print(d['name'])
    print(d[1], d[12])
    print('name' in d)
