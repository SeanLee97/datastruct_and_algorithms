# -*- coding: utf-8 -*-

# 求回文数

def ispn(num):
    origin = num
    t = 0
    while num != 0:
        t = t*10 + num%10
        num //= 10
    
    if origin == t:
        return True
    return False

print(ispn(32123))
print(ispn(321))
