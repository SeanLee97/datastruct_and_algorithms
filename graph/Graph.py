# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 封装了图常用接口

class Graph(object):
    def __init__(self, direction=True):
        self.direction = direction # 是否是有向图
        self.vertex = []
        self.edge = {}
    
    # 添加边
    def add_edge(self, u, v, w=1):
        if u not in self.vertex:
            self.vertex.append(u)
        if v not in self.vertex:
            self.vertex.append(v)
        self.edge[(u, v)] = w

    # 获取顶点字典
    # @param reverse: if True return {v: vid} else return {vid: v}
    def get_vertex_map(self, reverse=True):
        if not reverse:
            vertex = dict(zip(range(len(self.vertex)), self.vertex))
        else:
            vertex = dict(zip(self.vertex, range(len(self.vertex)))) 
        return vertex

    # 获取邻接矩阵
    def get_matrix(self):
        vertex = self.get_vertex_map(reverse=False)
        n = len(vertex)
        mat = [[0 for x in range(n)] for x in range(n)]
        for i in range(n):
            for j in range(n):
                if (vertex[i], vertex[j]) in self.edge:
                    mat[i][j] = self.edge[(vertex[i], vertex[j])]
                    if not self.direction:
                        mat[j][i] = self.edge[(vertex[i], vertex[j])]
        return mat

    # 获取邻接表
    def get_list(self):
        vertex = self.get_vertex_map()
        n = len(vertex)
        lst = {}
        for e in self.edge:
            u = vertex[e[0]]
            v = vertex[e[1]]
            if u not in lst:
                lst[u] = [v]
            else:
                lst[u].append(v)
            if not self.direction:
                if v not in lst:
                    lst[v] = [u]
                else:
                    lst[v].append(u)
        return lst

    # BFS
    def bfs(self, root=None):
        if not self.direction:
            raise ValueError('dfs only support directed graph')
        g = self.get_list()
        visited = [False]*len(self.vertex)
        vdecode = self.get_vertex_map(reverse=False)
        if isinstance(root, str):
            vertex = self.get_vertex_map()
            root = vertex[root]
        else:
            root = list(g)[0]
        queue = [root]
        visited[root]
        result = []
        while len(queue) > 0:
            u = queue.pop(0)
            result.append(vdecode[u])
            if u not in g:
                continue
            for v in g[u]:
                if not visited[v]:      
                    queue.append(v)
                    visited[v] = True
        return result

    # DFS
    def dfs(self, root=None):
        if not self.direction:
            raise ValueError('dfs only support directed graph')
        def _dfs(root, lst, visited, result):
            if not visited[root]:
                result.append(root)
                if root in lst:
                    for v in lst[root]: 
                        _dfs(v, lst, visited, result)
                        visited[v] = True
        g = self.get_list()
        result = []
        visited = [False]*len(self.vertex)
        _dfs(list(g)[0], g, visited, result)
        vdecode = self.get_vertex_map(reverse=False)
        result = list(map(lambda x: vdecode[x], result))
        return result

    # kruskal 最小生成树
    def kruskal(self):
        if self.direction:
            raise ValueError('kruskal only support undirected graph')
        
        def find_parent(parent, x):
            if x == parent[x]:
                return x
            return find_parent(parent, parent[x])

        def union(parent, rank, x, y):
            xroot = find_parent(parent, x)
            yroot = find_parent(parent, y)
            if xroot > yroot:
                parent[yroot] = xroot
            else:
                if rank[yroot] == rank[xroot]:
                    rank[yroot] += 1
                parent[xroot] = yroot
            
        # sort by weight ASC
        edge = sorted(self.edge.items(), key=lambda x: x[1])
        elist = [e[0] for e in edge]
         
        vertex = self.get_vertex_map()
        vdecode = self.get_vertex_map(reverse=False)
 
        result = []
        parent = []
        rank = []
        
        for k, v in vertex.items():
            parent.append(v)
            rank.append(0)

        i = 0
        e = 0
        # 边数 = 顶点数 - 1
        while e < len(self.vertex) - 1:
            (u, v) = elist[i]
            u = vertex[u]
            v = vertex[v]
            w = self.edge[elist[i]]
            i += 1
            x = find_parent(parent, u)
            y = find_parent(parent, v)
            if x!=y:
                # 没有环
                e += 1
                result.append([vdecode[u], vdecode[v], w])
                # 合并
                union(parent, rank, x, y)
        return result

    # Prim 求解最小生成树
    def prim(self):
        def min_dist(vsize, dist, visited):
            u = -1
            mindist = float('inf')
            for i in range(vsize):
                if not visited[i] and dist[i] < mindist:
                    mindist = dist[i]
                    u = i
            return u
       
        vsize = len(self.vertex)
        dist = [float('inf')]*vsize
        visited = [False]*vsize
        dist[0] = 0
        # 记录父节点
        parent = [None]*vsize
        parent[0] = -1

        matrix = self.get_matrix()
        for i in range(vsize):
            u = min_dist(vsize, dist, visited)
            visited[u] = True

            # 寻找下一结点，并选择距离小的结点
            for v in range(vsize):
                # matrix[u][v] > 0 保证了结点与当前结点是联通的
                if not visited[v] and matrix[u][v] > 0 and dist[v] > matrix[u][v]:
                    dist[v] = matrix[u][v]
                    parent[v] = u   
        vdecode = self.get_vertex_map(reverse=False) 
        result = []
        for i  in range(1, vsize):
            result.append([vdecode[parent[i]], vdecode[i], matrix[i][parent[i]]])
        return result

if __name__ == '__main__':
    g = Graph(direction=False)
    g.add_edge('a', 'b', 2)
    g.add_edge('a', 'd', 1)
    g.add_edge('b', 'c', 5)
    g.add_edge('c', 'd', 3)
    print(g.get_matrix())
    print(g.get_list())
    #print(g.bfs('a'))
    #print(g.dfs())
    print(g.kruskal())
    print(g.prim()) 
