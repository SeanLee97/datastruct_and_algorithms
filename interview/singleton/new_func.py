# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orgi = super(Singleton, cls)
            cls._instance = orgi.__new__(cls, *args, **kw)
        return cls._instance

class MyCls(Singleton):
    a = 1

cls = MyCls()
print(cls.a)
