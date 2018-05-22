# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Kruskal解决无向图最小生成树(并查集作为主要数据结构)
'''

from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.vertex = set()
        self.edge = []

    # u - source vertex
    # v - target vertex
    # w - weight
    def add_edge(self, u, v, w=0):
        self.vertex.add(u)
        self.vertex.add(v)
        self.edge.append([u, v, w])


    def find_parent(self, parent, i):
        j = i 
        while parent[j] != j:
            j = parent[j]
        x = i
        while x != j:
            y = parent[x]
            parent[x] = j
            x = y
        return x

    '''
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])
    '''

    def union(self, parent, rank, x, y):
        x_set_flag = self.find_parent(parent, x)
        y_set_flag = self.find_parent(parent, y)
        
        if rank[x_set_flag] < rank[y_set_flag]:
            # y_set_flag是大集合的代表
            # 小集合往大集合并,可知y_set_flag是大集合的代表,故小集合的代表应该换成大集合的代表
            parent[x_set_flag] = y_set_flag
        else:
            # x_set_flag是大集合的代表
            if rank[x_set_flag] == rank[y_set_flag]:
                # 如果集合大小相等，因为选择了x_set_flag作为代表,则x_set_flag大表的值应该+1
                rank[x_set_flag] += 1
            # x_set_flag是大集合的代表，故y_set_flag的代表值为x_set_flag
            parent[y_set_flag] = x_set_flag            

    # kruskal求最小生成树
    def kruskal(self):
        result = []
        i = 0
        e = 0
        # sorted(asc) by weight
        self.edge = sorted(self.edge, key=lambda x: x[2])
        #print(self.edge)
        parent = []
        rank = []
        for v in range(len(self.vertex)):
            parent.append(v)
            rank.append(0)

        # elen = vlen - 1
        while e < len(self.vertex) - 1:
            u, v, w = self.edge[i]
            i += 1

            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
 
            if x != y: # 说明没有环
                e = e + 1
                result.append([u, v, w])
                # 合并
                self.union(parent, rank, x, y)
        return result

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)    

    mst = g.kruskal()
    print(mst)
