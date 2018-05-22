# -*- coding: utf-8 -*-

def solution():
    raw = input()
    secret = ''
    for s in raw:   
        if (ord(s) >= ord('a') and ord(s) <= ord('z')) or ord(s) >= ord('A') and ord(s) <= ord('Z'):
            if ord(s) == ord('z'):
                secret += chr(ord('a'))
            elif ord(s) == ord('Z'):
                secret += chr(ord('A'))
            else:
                secret += chr(ord(s)+1)
        else:
            secret += s
    print(secret)

solution()