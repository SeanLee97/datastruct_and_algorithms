# -*- coding: utf-8 -*-

import math

def solution(n):
    if n <= 1:
        return None
    if n > 5:
        elsewise = 1
        while n > 0:
            n = n-3
            if n >= 3:
                elsewise *= 3
            else:
                elsewise *= (n+3)
                break
    else:
        n1 = math.ceil(n/2)
        n2 = n-n1
        elsewise = n1 * n2
    return elsewise

if __name__ == '__main__':
    print(solution(100))
    
