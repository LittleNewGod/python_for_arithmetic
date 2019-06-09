# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day97-最大正方形
# Author:       xin
# Date:         2019/6/9
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4

#思路：
# dp表的思想，dp里面存储以该点作为右下角端点的正方形的边长最大值，然后分情况讨论。matrix为0的点铁组成不了矩形，为1的点至少能组成一个1x1的矩形，然后根据dp（i-1,j-1）(i-1,j)(i,j-1)的值判断能不能组成一个更大的正方形,画个图可以发现，组成的新矩形的边长为他仨里面的最小值+1。

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        res = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        if dp[i - 1][j - 1] >= 0 and dp[i - 1][j] >= 0 and dp[i - 1][j - 1] >= 0:
                            dp[i][j] = 1 + min(int(dp[i - 1][j - 1]), dp[i - 1][j], dp[i][j - 1])
                        else:
                            dp[i][j] = 1
                res = max(res, dp[i][j])
        return res ** 2


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s= Solution()
print(s.maximalSquare(matrix))