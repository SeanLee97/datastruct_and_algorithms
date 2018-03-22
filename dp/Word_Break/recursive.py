# !/usr/bin/env python
# -*- coding: utf-8 -*-

vocab = ["mobile","samsung","sam","sung",
         "man","mango","icecream","and",
         "go","i","like","ice","cream"]

def f(inp):
    n = len(inp)
    if n == 0:
        return True
    for i in range(n+1):
        if inp[0:i] in vocab and f(inp[i:]):
            return True
    return False
    
 
inp = 'ilikesamsungandicecream'
print(f(inp))
