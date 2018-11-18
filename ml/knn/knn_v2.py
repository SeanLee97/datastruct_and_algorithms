# -*- coding: utf-8 -*-

import math
from collections import defaultdict

class KNN(object):
    def __init__(self, topk=3):
        self.data = None
        self.store = {}
        self.topk = topk

    def build_kdtree(self, points, depth=0):
        n = len(points)
        if n <= 0:
            # 如果当前子空间已经没有点了则构建过程结束
            return None
        
        # 计算当前选择的坐标轴
        axis = depth % 2
        # 对当前子空间的点根据当前选择轴的值进行排序
        sorted_points = sorted(points, key=lambda point: point[axis])
        # 中位数取排序后坐标点的中间位置的数
        median = n // 2
        
        return {
            # 当前根结点
            'point': sorted_points[median],
            # 将超平面左边的点交由左子结点递归操作
            'left': self.build_kdtree(sorted_points[:median], depth+1),
            # 同理，将超平面右边的点交由右子结点递归操作
            'right': self.build_kdtree(sorted_points[median+1:], depth+1)
        }

    def distance(self, p1, p2):
        if p1 is None or p2 is None:
            return 0

        x1, y1 = p1
        x2, y2 = p2

        x_ = x2 - x1
        y_ = y2 - y1

        return math.sqrt(x_**2 + y_**2)    

    def closer_distance(self, point, p1, p2):

        d1 = self.distance(point, p1)
        d2 = self.distance(point, p2)

        if p1 is None:
            return (p2, d2)
        if p2 is None:
            return (p1, d1)

        return (p1, d1) if d1 < d2 else (p2, d2)
    
    def kdtree_closest_point(self, root, point, depth=0):
        if root is None:
            return None
            
        axis = depth % 2

        next_branch = None
        opposite_branch = None
        
        # 以下主要是比较当前点到根结点和两个子结点之间的距离
        if point[axis] < root['point'][axis]:
            next_branch = root['left']
            opposite_branch = root['right']
        else:
            next_branch = root['right']
            opposite_branch = root['left']
        
        best, closer_dist = self.closer_distance(
            point, 
            self.kdtree_closest_point(
                next_branch, 
                point, 
                depth + 1),
            root['point']
        )

        if self.distance(point, best) > abs(point[axis] - root['point'][axis]):

            best, closer_dist = self.closer_distance(
                point, 
                self.kdtree_closest_point(
                    opposite_branch,
                    point,
                    depth + 1),
                best
            )

        # 储存距离，留作投票用
        if best in self.store and self.store[best] > closer_dist:
            self.store[best] =  closer_dist
        else:
            self.store[best] = closer_dist

        return best

    def fit(self, X, y):
        self.data = dict(zip(X, y))
        self.kdtree = self.build_kdtree(X)

    def predict(self, point):
        # best 是最邻近的点
        best = self.kdtree_closest_point(self.kdtree, point)

        sorted_stores = sorted(self.store.items(), key=lambda x: x[1])[:self.topk]
        counter = defaultdict(int)
        for candidates, score in sorted_stores:
            counter[self.data[candidates]] += 1

        # 按照投票数降序排列
        sorted_counter = sorted(counter.items(), key=lambda x: -x[1])
        counter = list(counter.items())

        if len(counter) > 1:
            if counter[0][1] != counter[1][1]:
                best = counter[0][1]
        
        return self.data[best]

if __name__ == '__main__':

    # 训练数据
    points = [(1, 1), (1, 1.2), (0, 0), (0, 0.2), (3, 0.5), (3.3, 0.9)]
    labels = ['A', 'A', 'B', 'B', 'C', 'C']

    knn = KNN(topk=3)
    # 开始训练
    knn.fit(points, labels)
    # 预测
    label = knn.predict((0.9,0.9))
    print(label)
