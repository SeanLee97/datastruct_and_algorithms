# -*- coding: utf-8 -*- 
"""题目描述
表达式求值

逆波兰式（后缀式）+ 栈求解
"""


# 符号优先级的比较
def precede(x, y):
    if x == '(':
        x = 0
    elif x in ['+', '-']:
        x = 1
    elif x in ['*', '/']:
        x = 2
    else:
        x = -2
    
    if y in ['+', '-']:
        y = 1
    elif y in ['*', '/']:
        y = 2
    elif y == '(':
        y = 3
    else:
        y = -1
    return x >= y

# 中缀转后缀
def mid_to_post(inp):
    post = []
    stack = ["#"]
    for i in range(len(inp)):
        print(stack)
        if inp[i] == ')':
            while len(stack) > 0 and stack[-1] != '(':
                post.append(stack.pop())
            if len(stack) > 0:
                stack.pop()
        elif inp[i] in ['+', '-', '*', '/', '(']:
            while len(stack) > 0  and precede(stack[-1], inp[i]):
                post.append(stack.pop())
            stack.append(inp[i])
        else:
           post.append(inp[i])
    while len(stack) > 0:
        post.append(stack.pop())
    return post

def calc(inp):
    if len(inp) == 0:
        return None
    stack = []
    post = mid_to_post(inp)    

    result = 0
    for e in post:
        if e == '#':
            break
        if e == '+':
            a = stack.pop()
            b = stack.pop()
            result = b + a
            stack.append(result)
        elif e == '-':
            a = stack.pop()
            b = stack.pop()
            result = b - a 
            stack.append(result)
        elif e == '*':
            a = stack.pop()
            b = stack.pop()
            result = b * a
            stack.append(result)
        elif e == '/':
            a = stack.pop()
            b = stack.pop()
            result = b / a
            stack.append(result)
        else:
            stack.append(int(e))
    return stack[-1]

if __name__ == '__main__':
     result = calc('(2+3-3)*2') 
     print(result)
