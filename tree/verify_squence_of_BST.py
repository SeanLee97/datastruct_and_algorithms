# -*- coding: utf-8 -*-

class Solution:
    def check(self, lst, L, R):
        if L >= R:
            return True
        idx = L
        while idx < R-1 and lst[idx] < lst[R]:
            idx += 1
        while idx < R-1 and lst[idx] > lst[R]:
            idx += 1
        if idx + 1 != R:
            return False
        return self.check(lst, L, idx-1) and self.check(lst, idx, R-1)
        
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.check(sequence, 0, len(sequence)-1)
