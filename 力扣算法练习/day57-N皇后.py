# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 8:38
# @Author  : Xin
# @File    : day57-N皇后.py
# @Software: PyCharm

# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#（day57-题目图）
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
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
# 解释: 4 皇后问题存在两个不同的解法。
import pysnooper
from itertools import permutations

class Solution(object):
    def __init__(self):
        self.res = []
        self.n = 0

    @pysnooper.snoop('log/day57.log', prefix="solveNQueens: ")
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        for vec in permutations(range(n)):
            # 这步比较关键,排除各种可能的对角线,好好思考一下就懂了
            if (n == len(set(vec[i] + i for i in range(n))) == len(set(vec[i] - i for i in range(n)))):
                self.generate_q(vec)
        return self.res

    # 拼接需要的输出结果,添加进self.res
    @pysnooper.snoop('log/day57.log', prefix="generate_q: ")
    def generate_q(self, vec):
        s = '.' * self.n
        a = []
        for i in vec:
            q = i * "." + 'Q' + (self.n - i - 1) * '.'
            a.append(q)
        self.res.append(a)

n=4
s= Solution()
print(s.solveNQueens(n))