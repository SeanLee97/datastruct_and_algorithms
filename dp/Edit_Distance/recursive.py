# !/usr/bin/env python
# -*- coding: utf-8 -*-

def edit(str1, str2, m, n):
    if m == 0 or n == 0:
        return abs(m-n)
    if str1[m-1] == str2[n-1]:
        return edit(str1, str2, m-1, n-1)
    else:
        return 1 + min(
            edit(str1, str2, m-1, n),  # remove
            edit(str1, str2, m, n-1),  # insert
            edit(str1, str2, m-1, n-1) # replace
        )   

src = 'pair'
tgt = 'peer'

print(edit(src, tgt, len(src), len(tgt)))

