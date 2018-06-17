# -*- coding: utf-8 -*-

"""题目描述
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
"""

from collections import OrderedDict
class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s) < 1 or len(s) > 10000:
            return -1
        # write code here
        table = OrderedDict()
        postable = {}
        for idx, ch in enumerate(s):
            if ch not in table:
                table[ch] = 1
                postable[ch] = idx
            else:
                table[ch] += 1

        for k, v in table.items():
            if v == 1:
                return postable[k]
        return -1

if __name__ == '__main__':
    s = Solution()
    n = s.FirstNotRepeatingChar('NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp')
    print(n)
