# -*- coding: utf-8 -*-

import random

def shuffle(lst):
    for i in range(len(lst)-1, -1, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

if __name__ == '__main__':
    lst = [2, 3, 1, 8]
    shuffle(lst)
    print(lst)
