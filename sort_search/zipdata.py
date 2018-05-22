# -*- coding: utf-8 -*-

x = ['a', 'b', 'c', 'd']
y = [2, 1, 5, 3]

data = zip(x, y)
data_ = sorted(data, key=lambda x: x[1], reverse=True)

x, y = zip(*data_)

print(x) # ('c', 'd', 'a', 'b')
print(y) # (5, 3, 2, 1)
