# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 19:07
# @Author  : Xin
# @File    : day35-螺旋矩阵.py
# @Software: PyCharm

# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]

#解法一：根据索引的变化来循环每个元素
# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         if matrix == []:
#             return []
#         m = len(matrix)
#         n = len(matrix[0])
#         numbers = m*n
#         res = []
#         temp = 0
#         i = j = 0
#         while numbers:
#             res.append(matrix[i][j])
#             numbers -= 1
#             if i == temp and j!=n-1:
#                 j+=1
#             elif j==n-1 and i!=m-1:
#                 i+=1
#             elif i == m-1 and j!=temp:
#                 j-=1
#             else:
#                 if i == temp+1:
#                     m -= 1
#                     n -= 1
#                     temp += 1
#                     i = j = temp
#                     continue
#                 i-=1
#         return res
#
# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# s = Solution()
# print(s.spiralOrder(matrix))

#解法二：
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 取首行，去除首行后，对矩阵翻转来创建新的矩阵，
        # 再递归直到新矩阵为[],退出并将取到的数据返回
        ret = []
        if matrix == []:
            return ret
        ret.extend(matrix[0])  # 上侧
        new = [reversed(i) for i in matrix[1:]]
        if new == []:
            return ret
        a = [i for i in zip(*new)]
        r = self.spiralOrder(a)
        ret.extend(r)
        return ret

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s = Solution()
print(s.spiralOrder(matrix))