# -*- coding: utf-8 -*-


def solution(lst, n):
    steps = []
    for idx, v in enumerate(lst):
        step = idx+1
        for i in range(v):
            print(lst[i], n)
            if step+lst[i] >= n:
                steps.append(step)
            step += 1
    return min(steps)

if __name__ == '__main__':
    lst = [2, 3, 1, 1, 4]
    n = len(lst)
    result = solution(lst, n)
    print(result)
