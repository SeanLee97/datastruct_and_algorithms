# coding: utf-8 -*-

def singleton(cls, *args, **kw):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return getinstance

@singleton
class MyClass:
    a = 1

