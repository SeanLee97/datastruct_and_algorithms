# -*- coding: utf-8 -*-

""" 题目描述
有n个顾客同时等待一项服务，顾客i需要的服务时间为ti，1≤i≤n，共有s处可以提供此项服务。应如何安排n个顾客的服务次序才能使平均等待时间达到最小？平均等待时间是n个顾客等待服务时间的总和除以n

分析：
为了平均等待时间最少，当然是用时少的服务先执行。所以对服务时间最短的顾客先服务的贪心选择策略，做完第一次选择后，原问题T变成了需对n—1个顾客服务的新问题T’，规模一直缩小，符合贪心算法
"""

class Solution(object):
    def greedy(self, client, s):
        # client -> list 客户等待的时间
        # s 服务点数目
        client.sort()     # 排序
        service = [0]*s   # 服务点每个客户等待时间
        waitsum = [0]*s   # 服务点顾客等待时间总和
        n = len(client)
        j = 0 # 记录服务点ID
        for i in range(n):
            service[j] += client[i]
            waitsum[j] += service[j]
            j+=1
            if j == s:
                j = 0
        avgtime = sum(waitsum) / n    # 每个客户平均等待时间
        return avgtime

if __name__ == '__main__':
    so = Solution()
    lst = [56, 12, 1, 99, 1000, 234, 33, 55, 99, 812]  # 用户等待时间
    s = 2   # 服务点个数
    t = so.greedy(lst, s) 
    print(t)
        


