# !/usr/bin/env python
# -*- coding: utf-8 -*-

def f(Vt, Wt, W, n):
    if n == 0:
        return 0

    if Wt[n-1] > W:
        return f(Vt, Wt, W, n-1)
    
    # 1. 当不选择当前物品时，最大价值=先前最大价值
    # W-0：为了方便理解总容量的变化，由于不选择当前物品所以剩余总容量没有发生变化
    c1 = f(Vt, Wt, W-0, n-1) 
    # 2. 当选择了当前物品时，最大价值=当前价值+先前最大价值
    # W-Wt[n-1]：由于选择了当前物品，所以剩余总容量已经发生了变化
    c2 = Vt[n-1] + f(Vt, Wt, W-Wt[n-1], n-1)
    return max(c1, c2)

Vt = [60, 100, 120] # 价值
Wt = [10, 20, 30] # 容量
W = 50  # 总容量
print(f(Vt, Wt, W, len(Wt)))
