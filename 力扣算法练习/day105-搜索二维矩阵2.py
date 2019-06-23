# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day105-搜索二维矩阵2
# Author:       xin
# Date:         2019/6/17
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。

#解法一：搜索全数组，效率很低
# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix:
#             return False
#         for i in range(len(matrix)):
#             if target in matrix[i]:
#                 return True
#         return False
#
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5
# s= Solution()
# print(s.searchMatrix(matrix,target))

#解法二：分治法。
# 左下角的元素是这一行中最小的元素，同时又是这一列中最大的元素。比较左下角元素和目标：
# 若左下角元素等于目标，则找到
# 若左下角元素大于目标，则目标不可能存在于当前矩阵的最后一行，问题规模可以减小为在去掉最后一行的子矩阵中寻找目标
# 若左下角元素小于目标，则目标不可能存在于当前矩阵的第一列，问题规模可以减小为在去掉第一列的子矩阵中寻找目标
# 若最后矩阵减小为空，则说明不存在
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
s= Solution()
print(s.searchMatrix(matrix,target))