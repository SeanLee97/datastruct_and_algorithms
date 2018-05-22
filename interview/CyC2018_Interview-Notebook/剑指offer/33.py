# -*- coding: utf-8 -*-

"""题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。假设输入的数组的任意两个数字都互不相同

解题思路：
在后序遍历得到的序列中， 最后一个数字是树的根结点的值。数组中前面的数字可以分为两部分： 第一部分是左子树结点的值，它们都比根结点的值小： 第二部分是右子树结点的值，它们都比根结点的值大。
"""

class Solution:

    def check(self, sequence, start, end):
        if start >= end:
            return True
        idx = start
        # 从左到右遍历，直到找到第一个比根结点(sequence[end])大的数
        while idx < end -1 and sequence[idx] < sequence[end]:
            idx += 1
        # 从idx处开始从左到右遍历，直到找到第一个比根结点小的值
        while idx < end -1 and sequence[idx] > sequence[end]:
            idx += 1
        # 如果当前层满足二叉数的后序遍历则有 idx + 1 = end
        if idx+1 != end:
            return False
        return self.check(sequence, start, idx-1) and self.check(sequence, idx, end-1) 

    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence is None or len(sequence) == 0:
            return False
        return self.check(sequence, 0, len(sequence)-1)

if __name__ == '__main__':
    s = Solution()
    flag = s.VerifySquenceOfBST([3,1,2])
    print(flag)
