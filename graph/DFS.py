# !/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
class Graph(object):
    def __init__(self):
        self.vertex = set()
        self.edge = defaultdict(list)
    def addEdge(self, u, v):
        self.vertex.add(u)
        self.vertex.add(v)
        self.edge[u].append(v)

    def DFS(self, v):
        visited = defaultdict(bool)
        for _v in self.vertex:
            visited[_v] = False
        lst = []
        self._DFS(v, visited, lst)
        return lst
    
    def _DFS(self, v, visited, lst):
        visited[v] = True
        lst.append(v)
        for i in self.edge[v]:
            if not visited[i]:
                self._DFS(i, visited, lst)
        

g = Graph()
g.addEdge('A', 'B')
g.addEdge('B', 'A')
g.addEdge('A', 'C')
g.addEdge('C', 'A')
g.addEdge('B', 'D')
g.addEdge('D', 'B')
print(g.DFS('A'))
