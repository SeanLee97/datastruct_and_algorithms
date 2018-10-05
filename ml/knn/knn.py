# -*- coding:utf-8 -*-

import math
from collections import defaultdict

class KNN(object):
    def __init__(self, k=2):
        self.data = None
        self.k = k

    def distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        x_ = x2 - x1
        y_ = y2 - y1

        return math.sqrt(x_**2 + y_**2)        

    def fit(self, X, y):
        self.data = dict(zip(X, y))

    def predict(self, point):
        distances = {}
        
        for p, _ in self.data.items():
            distances[p] = self.distance(p, point)

        sort_distances = dict(sorted(distances.items(), key=lambda x: x[1]))
        topk = defaultdict(int)
        for idx, (p, v) in enumerate(sort_distances.items()):
            if idx == self.k - 1:
                break
            topk[self.data[p]] += 1

        topk = sorted(topk.items(), key=lambda x: -x[1])
        return topk[0][0]

if __name__ == '__main__':
    points = [(1, 1), (1, 1.2), (0, 0), (0, 0.2), (3, 0.5), (3.3, 0.9)]
    labels = ['A', 'A', 'B', 'B', 'C', 'C']

    knn = KNN()
    knn.fit(points, labels)
    label = knn.predict((0.9,0.7))
    print(label)
