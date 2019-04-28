# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 8:51
# @Author  : Xin
# @File    : day48-搜索二维矩阵.py
# @Software: PyCharm


# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 示例 2:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false


#解法一：利用矩阵升序的特点先作好判断范围利用内置函数来查找
# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         # matrix = [[]
#         # ]
#         if not matrix or not matrix[0]:
#             return False
#         matrix_len = len(matrix)-1
#         matrix_child_len = len(matrix[0])-1
#
#         if matrix[0][0] <= target <= matrix[matrix_len][matrix_child_len]:
#             for i in range(matrix_len+1):
#                 if target in matrix[i]:
#                     return True
#
#         return False
#
# matrix = [
#             [1, 3, 5, 7],
#             [10, 11, 16, 20],
#             [23, 30, 34, 50]
#         ]
# target = 1
# s = Solution()
# print(s.searchMatrix(matrix,target))


#解法二：大致上跟解法一差不多，就是在查找目标数利用的是二分查找
# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         # matrix = [[]
#         # ]
#         if not matrix or not matrix[0]:
#             return False
#         matrix_len = len(matrix)-1
#         matrix_child_len = len(matrix[0])-1
#
#         if matrix[0][0] <= target <= matrix[matrix_len][matrix_child_len]:
#             for i in range(matrix_len+1):
#                 l=0
#                 r = matrix_child_len
#                 while l<=r:
#                     mid =(l+r) // 2
#                     if matrix[i][mid]==target:
#                         return True
#                     elif matrix[i][mid]<target:
#                         l = mid+1
#                     else:
#                         r = mid-1
#
#
#         return False
#
# matrix = [
#             [1, 3, 5, 7],
#             [10, 11, 16, 20],
#             [23, 30, 34, 50]
#         ]
# target = 31
# s = Solution()
# print(s.searchMatrix(matrix,target))

#解法三，直接省去那些判断，直接使用二分查找，一维数组的查找使用二分法，矩阵只是需要将index与行列进行转换n×m矩阵的算法复杂度为$O(logn + logm)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        rows = len(matrix)
        cols = len(matrix[0])
        lens = rows * cols

        l, r = 0, lens - 1
        while l <= r:

            mid = (l + r) // 2
            i = mid // cols
            j = mid % cols

            if matrix[i][j] == target: return True

            if target < matrix[i][j]:
                r = mid - 1
            else:
                l = mid + 1
        return False

matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
target = 31
s = Solution()
print(s.searchMatrix(matrix,target))