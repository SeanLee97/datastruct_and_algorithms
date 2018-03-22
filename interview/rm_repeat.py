# -*- coding: utf-8 -*-

def rm_repeat(lst):
    return list(dict.fromkeys(lst))

lst = [2,3,2,1]
print(rm_repeat(lst))
