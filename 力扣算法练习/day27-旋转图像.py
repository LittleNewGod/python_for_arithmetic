# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 22:15
# @Author  : Xin
# @File    : day27-旋转图像.py
# @Software: PyCharm


# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:
#
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

#解法：这个旋转90度是有一定的规律的，可以考虑旋转四角，逐个旋转，由外到内，一层层替换

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        start = 0
        matrix_len = len(matrix)-1
        while start<=matrix_len:
            i = start
            j =matrix_len
            while i < matrix_len:
                temp = matrix[start][i]                     #左上
                matrix[start][i] = matrix[j][start]         #左上=左下
                matrix[j][start]=matrix[matrix_len][j]      #左下=右下
                matrix[matrix_len][j]=matrix[i][matrix_len] #右下=右上
                matrix[i][matrix_len]=temp                  #右上=左上

                i+=1
                j-=1
            start+=1
            matrix_len-=1

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
s = Solution()
s.rotate(matrix)
print(matrix)

