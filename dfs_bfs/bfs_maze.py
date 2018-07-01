# -*- coding: utf-8 -*-

"""
BFS可以用来解决迷宫问题，想比DFS，BFS采用迭代的方式更容易理解

0, 1, 0, 0, 0,

0, 1, 0, 1, 0,

0, 0, 0, 0, 0,

0, 1, 1, 1, 0,

0, 0, 0, 1, 0,

如图表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，
不能斜着走，要求编程序找出从左上角到右下角的最短路线
分析：
对应于《迷宫问题》，你可以这么认为，节点就是迷宫路上的每一个格子（非墙），
走迷宫的时候，格子间的关系是什么呢？按照题目意思，我们只能横竖走，
因此我们可以这样看，格子与它横竖方向上的格子是有连通关系的，
只要这个格子跟另一个格子是连通的，那么两个格子节点间就有一条边。
搜索顺序就是第一层->第二层->第三层->第N层这样子。
所以根据广度优先搜索的话，搜索到终点时，该路径一定是最短的。

详细题目：
https://blog.csdn.net/llzhh/article/details/51067351
http://rapheal.iteye.com/blog/1526861
"""

import time

def solution(maze):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 只能横着走竖着走
    m = len(maze)
    n = len(maze[0])
    visit = [[False for x in range(n)] for x in range(m)]
    q = [(0, 0, 1)]
    visit[0][0] = True

    while len(q) > 0:
        (i, j, step) = q[0]
        flag = False
        for pos in direction:
            x = i + pos[0]
            y = j + pos[1]
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                continue
            if not visit[x][y] and maze[x][y] == 0:
                q.append((x, y, step+1))
                visit[x][y] = True

            if x == m-1 and y == n-1:
                flag = 1
                break
        if flag:
            return q[-1][2]

        q = q[1:]
        #print(q)
        #time.sleep(1)
    return -1

if __name__ == '__main__':
    maze = [[0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0]]
    step = solution(maze)
    print(step)





