# -*- coding: utf-8 -*-

import math
import pprint
from collections import defaultdict

class KNN(object):
    def __init__(self, kd=2):
        self.kd = kd
        self.data = None

    def build_kdtree(self, points, depth=0):
        n = len(points)
        if n <= 0:
            return None
        
        axis = depth % self.kd
        sorted_points = sorted(points, key=lambda point: point[axis])
        
        median = n // 2
        return {
            'point': sorted_points[median],
            'left': self.build_kdtree(sorted_points[:median], depth+1),
            'right': self.build_kdtree(sorted_points[median+1:], depth+1)
        }
        
    def fit(self, X, y):
        self.data = dict(zip(X, y))
        self.kdtree = self.build_kdtree(X)
        #pprint.pprint(self.kdtree)

    def distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        x_ = x2 - x1
        y_ = y2 - y1

        return math.sqrt(x_**2 + y_**2)    

    def closer_distance(self, point, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        d1 = self.distance(point, p1)
        d2 = self.distance(point, p2)

        if d1 < d2:
            return p1
        else:
            return p2
    
    def kdtree_closest_point(self, root, point, depth=0):
        if root is None:
            return None
        axis = depth % self.kd

        next_branch = None
        opposite_branch = None

        if point[axis] < root['point'][axis]:
            next_branch = root['left']
            opposite_branch = root['right']
        else:
            next_branch = root['right']
            opposite_branch = root['left']
        
        best = self.closer_distance(point, 
                                    self.kdtree_closest_point(next_branch, 
                                                              point, 
                                                              depth + 1),
                                    root['point'])

        if self.distance(point, best) > abs(point[axis] - root['point'][axis]):
            best = self.closer_distance(point, 
                                        self.kdtree_closest_point(opposite_branch,
                                                                  point,
                                                                  depth + 1),
                                        best)

        return best

    def predict(self, point):
        best = self.kdtree_closest_point(self.kdtree, point)
        return self.data[best]

if __name__ == '__main__':
    points = [(1, 1), (1, 1.2), (0, 0), (0, 0.2), (3, 0.5), (3.3, 0.9)]
    labels = ['A', 'A', 'B', 'B', 'C', 'C']

    knn = KNN()
    knn.fit(points, labels)
    label = knn.predict((0.9,0.7))
    print(label)

