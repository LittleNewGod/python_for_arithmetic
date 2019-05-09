# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 18:01
# @Author  : Xin
# @File    : day63-N皇后2.py
# @Software: PyCharm

# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# day63-题目图
# 上图为 8 皇后问题的一种解法。
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 示例:
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

#解法一：完全复制解法二，很慢
#from itertools import permutations
# class Solution(object):
#     def __init__(self):
#         self.res = []
#         self.n = 0
#     def totalNQueens(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         self.n = n
#         for vec in permutations(range(n)):
#             # 这步比较关键,排除各种可能的对角线,好好思考一下就懂了
#             if (n == len(set(vec[i] + i for i in range(n))) == len(set(vec[i] - i for i in range(n)))):
#                 self.generate_q(vec)
#         #return self.res
#         return len(self.res)
#     # 拼接需要的输出结果,添加进self.res
#     def generate_q(self, vec):
#         s = '.' * self.n
#         a = []
#         for i in vec:
#             q = i * "." + 'Q' + (self.n - i - 1) * '.'
#             a.append(q)
#         self.res.append(a)
#
# n=4
# s= Solution()
# print(s.solveNQueens(n))


#解法二：
class Solution:
    def totalNQueens(self, n):
        if n < 1: return []  #
        self.count = 0
        shu = []  # 竖方向是否被攻击
        pie = []  # 撇方向是否被攻击  x y 坐标之和固定 x + y
        na = []  # 捺方向是否被攻击  x y 坐标之差固定 x - y

        self.DFS(n, shu, pie, na)

        return self.count

    def DFS(self, n, shu, pie, na):  # 深度优先搜索
        p = len(shu)  # 从 1 -> n
        if p == n:
            self.count += 1  # 每层有且只能放一个
            return
        for q in range(n):  # 看成 x  每层枚举可能的 x
            if q not in shu and p - q not in na and p + q not in pie:  # 这一层存在可能位置，向下层搜索
                self.DFS(n, shu + [q], pie + [p + q], na + [p - q])  # 深度优先搜索  将被攻击的 坐标记录下来

n=4
s= Solution()
print(s.solveNQueens(n))