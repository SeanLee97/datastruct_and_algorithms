# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Prim求最小生成树，图用邻接矩阵表示

INF = 65535

class Graph(object):
    def __init__(self, vsize):
        self.vsize = vsize
        # 邻接矩阵
        self.matrix = [[0 for x in range(vsize)] for _ in range(vsize)]

    def echo(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.vsize):
            print(parent[i],"-",i,"\t",self.matrix[i][parent[i]])

    def mindist(self, distance, visit):
        mindistance = INF
        u = -1
        for v in range(self.vsize):
            if distance[v] < mindistance and not visit[v]:
                mindistance = distance[v]
                u = v
        return u

    def prim(self):
        # 初始距离无穷
        distance = [INF]*self.vsize
        # 选取第一个节点被访问
        distance[0] = 0
        # 节点是否被访问
        visit = [False]*self.vsize
        # 
        parent = [None]*self.vsize
        parent[0] = -1

        for i in range(self.vsize):
            u = self.mindist(distance, visit)
            visit[u] = True

            # 寻找下一个节点，并选择距离小的节点
            for v in range(self.vsize):
                # self.matrix[u][v] > 0 : > 0 保证了节点和当前选定节点是连通的
                if self.matrix[u][v] > 0 and distance[v] > self.matrix[u][v] and not visit[v]:
                    distance[v] = self.matrix[u][v]
                    parent[v] = u
        self.echo(parent)

g  = Graph(5)
g.matrix = [ [0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
           ]
 
g.prim()
