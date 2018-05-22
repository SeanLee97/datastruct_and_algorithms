# -*- coding: utf-8 -*-

class Solution:
    def permutate(self, result, chars, begin):
        if len(chars) -1 == begin:
            result.append(''.join(chars))
        else:
            for i in range(begin, len(chars)):
                if (i != begin and chars[i] == chars[begin]):
                    continue
                chars[i], chars[begin] = chars[begin], chars[i]
                self.permutate(result, chars, begin+1)
                # 防止重复，还得将begin初的元素重新换回来
                chars[i], chars[begin] = chars[begin], chars[i]
    
    def Permutation(self, ss):
        # write code here
        chars = list(ss)
        result = []
        self.permutate(result, chars, 0)
        # 排序
        result = sorted(result, key=lambda x: [xx for xx in x])
        return result

if __name__ == '__main__':
    s = Solution()
    r = s.Permutation('abc')
    print(r)
