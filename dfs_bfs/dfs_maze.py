# -*- coding: utf-8 -*-

"""
这里用dfs求解迷宫最短路径问题,问题和bfs的一样，只是求法不同
"""
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(maze, i, j, m, n, step, visit):
    if i < 0 or i > m-1 or j < 0 or j > n-1 \
            or visit[i][j] or maze[i][j] == 1:
        return
    step += 1
    visit[i][j] = True
    if i == m-1 and j == n-1:
        dfs.minimum = min(step, dfs.minimum)
    global directions
    for pos in directions:
        dfs(maze, i+pos[0], j+pos[1], m, n, step, visit)

if __name__ == '__main__':
    maze = [[0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0]]
    dfs.minimum = float('inf')
    m = len(maze)
    n = len(maze[0])
    visit = [[False for x in range(n)] for x in range(m)]
    dfs(maze, 0, 0, m, n, 0, visit)
    print(dfs.minimum)

