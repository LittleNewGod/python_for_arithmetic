# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 8:39
# @Author  : Xin
# @File    : day49-组合.py
# @Software: PyCharm

# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n or k == 0:
            return []
        if k == 1:
            a=[[i] for i in range(1, n + 1)]
            return a
        if k == n:
            b =[[i for i in range(1, n + 1)]]
            return b

        answer = self.combine(n - 1, k)
        for item in self.combine(n - 1, k - 1):
            item.append(n)
            answer.append(item)

        return answer

n=4
k=2
s = Solution()
print(s.combine(n,k))
