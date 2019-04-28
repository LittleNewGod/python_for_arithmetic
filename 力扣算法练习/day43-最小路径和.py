# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 11:32
# @Author  : Xin
# @File    : day43-最小路径和.py
# @Software: PyCharm

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。


# 首先对于第一行和第一列进行处理.因为第一行只能通过向右走到达,第一列只能通过向下走到达,.遍历第一行,到达第一行某个位置的距离,等于到达前一格的距离加上本格距离.第一列同理.
#
# 对于不在第一行第一列的方格,使用双重循环.到达该方格的距离等于min(到达上一格的距离,到达左一格的距离)+本格距离.遍历完成后.最后一格上的数字即为到达最后一格的最短距离.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        for i in range(1,n):
            grid[0][i]+=grid[0][i-1]
        for j in range(1,m):
            grid[j][0]+=grid[j-1][0]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[m-1][n-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
s = Solution()
print(s.minPathSum(grid))
