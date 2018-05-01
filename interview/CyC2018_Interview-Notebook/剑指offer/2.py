# -*- coding: utf-8 -*-

""" 题目描述
  实现单例模式
"""

# 1. 类实现

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            origin = super(Singleton, cls)
            cls._instance = origin.__new__(cls, *args, **kwargs)
        return cls._instance

class MyCls(Singleton):
    a = 1

cls = MyCls()
print('cls.a', cls.a)
cls.a = 2
cls2 = MyCls()
print('cls2.a', cls2.a)

# 2. 装饰器实现
def singletone(cls, *args, **kwargs):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance

@singletone
class MyCls2(object):
   a = 1

cls = MyCls2()
print('cls.a', cls.a)
cls.a = 2
cls2 = MyCls2()
print('cls2.a', cls2.a)

# 3. 最简单的方式-通过模块来调用
