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
    
    def BFS(self, v):
        visited = defaultdict(bool)
        for _v in self.vertex:
            visited[_v] = False
        queue = [v]
        visited[v] = True
        lst = []
        while queue:
            #print('Q', queue)
            v = queue.pop(0)
            #print('Q_', queue)
            lst.append(v)
            for i in self.edge[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return lst

g = Graph()
g.addEdge('A', 'B')
g.addEdge('B', 'A')
g.addEdge('A', 'C')
g.addEdge('C', 'A')
g.addEdge('B', 'C')
g.addEdge('C', 'B')
g.addEdge('B', 'D')
g.addEdge('D', 'B')
print(g.BFS('A'))
