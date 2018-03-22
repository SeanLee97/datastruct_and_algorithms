# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 检测一个图是否有环

from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.vertex = set()
        self.edge = defaultdict(list)

    def add_edge(self, u, v):
        self.vertex.add(u)
        self.vertex.add(v)
        self.edge[u].append(v)

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
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent, parent[i])
    '''

    def union(self, parent, rank, x, y):
        x_set_flag = self.find_parent(parent, x)
        y_set_flag = self.find_parent(parent, y)

        if rank[x_set_flag] < rank[y_set_flag]:
        	parent[x_set_flag] = y_set_flag
        else:
        	parent[y_set_flag] = x_set_flag
        	if rank[x_set_flag] == rank[y_set_flag]:
        		rank[x_set_flag] += 1

    # 判断无向图是否有环
    def detect_cycle_undirect_graph(self):
        # init
        parent = []
        rank = []
        for i in range(len(self.vertex)):
        	parent.append(i)
        	rank.append(0)

        for i in self.edge:
            for j in self.edge[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, rank, x, y)

    # DFS 判断有向图是否有环
    def _detect_cycle_direct_graph(self, s, visited, record):
        visited[s] = True
        record[s] = True

        for v in self.edge[s]:
            if not visited[v]:
                if self._detect_cycle_direct_graph(v, visited, record):
                    return True
            # 检测是否已经记录过该点
            elif record[v]:
                return True
        record[s] = False
        return False

    def detect_cycle_direct_graph(self):
        visited = [False]*len(self.vertex)
        record = [False]*len(self.vertex)
        for v in self.vertex:
            if not visited[v]:
                if self._detect_cycle_direct_graph(v, visited, record):
                    return True
        return False


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)
    
    if g.detect_cycle_undirect_graph():
        print("Graph contains cycle")
    else :
        print("Graph does not contain cycle ")

    if g.detect_cycle_direct_graph():
        print("Graph contains cycle")
    else :
        print("Graph does not contain cycle ")
