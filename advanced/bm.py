# -*- coding: utf-8 -*-

"""
KMP的匹配是从模式串的开头开始匹配的，而1977年，
德克萨斯大学的Robert S. Boyer教授和J Strother Moore教授
发明了一种新的字符串匹配算法：Boyer-Moore算法，简称BM算法。
该算法从模式串的尾部开始匹配，且拥有在最坏情况下O(N)的时间复杂度。
在实践中，比KMP算法的实际效能高。

推荐阅读：
https://blog.csdn.net/wjy0330/article/details/39589743
"""
