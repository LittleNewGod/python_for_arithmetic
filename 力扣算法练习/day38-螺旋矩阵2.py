# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 20:27
# @Author  : Xin
# @File    : day38-螺旋矩阵2.py
# @Software: PyCharm

# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

#解法一：
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        c = 1
        c, j = 1, 0
        while c <= n * n:
            for i in range(j, n - j):
                matrix[j][i] = c
                c += 1
            for i in range(j + 1, n - j):
                matrix[i][n - j - 1] = c
                c += 1
            for i in range(n - j - 2, j - 1, -1):
                matrix[n - 1 - j][i] = c
                c += 1
            for i in range(n - j - 2, j, -1):
                matrix[i][j] = c
                c += 1
            j += 1

        return matrix
#[[1,2,3],[8,9,4],[7,6,5]]
n = 3
s = Solution()
print(s.generateMatrix(n))

#解法二：相比解法一更优化了，时间复杂度小了
# class Solution(object):
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         res = [[0 for i in range(n)] for i in range(n)]
#         i,j,di,dj=0,0,0,1
#         for number in range(1,n*n+1):
#             res[i][j]=number
#             if res[(i+di)%n][(j+dj)%n]!=0: #需要转向
#                 di,dj = dj,-di #0 1 变 1 0, 1 0 变 0 -1, 0 -1 变 -1, 0, -1 0 变 0 1
#             i+=di
#             j+=dj
#         return res
#
# #[[1,2,3],[8,9,4],[7,6,5]]
# n = 3
# s = Solution()
# print(s.generateMatrix(n))
