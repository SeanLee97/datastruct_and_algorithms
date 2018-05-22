# -*- coding: utf-8 -*-

def rep(inp):
    n = len(inp)
    i = n-1
    while i>=0:
        if inp[i] == ' ':
            inp = inp[:i] + '%20' + inp[i+1:]
        i-=1
    return inp

s = 'We Are Happy. '
print(rep(s))
