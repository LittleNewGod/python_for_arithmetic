# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 8:20
# @Author  : Xin
# @File    : day81-岛屿数量.py
# @Software: PyCharm

# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3

#解法一：DFS递归
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         try:
#             m = len(grid)
#             n = len(grid[0])
#         except:
#             return 0
#
#         # -------------------------DFS 开始------------------------
#         # 定义dfs递归方程
#         def dfs(i, j):
#             if 0 <= i < m and 0 <= j < n and int(grid[i][j]):
#                 grid[i][j] = '0'
#                 for a, b in ((1, 0), (0, -1), (-1, 0), (0, 1)):
#                     dfs(i + a, j + b)
#
#         # ---------------------------------------------------------
#
#         r = 0
#         for i in range(m):
#             for j in range(n):
#                 r += int(grid[i][j])
#                 dfs(i, j)  # 调用dfs沉没一整块陆地
#         return r
#
# grid =[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# s= Solution()
# print(s.numIslands(grid))


#解法二：BFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        res = 0
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    res += 1
                    queue = [(i, j)]
                    while queue:
                        a, b = queue.pop(0)
                        for dx, dy in d:
                            x = a + dx
                            y = b + dy
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                grid[x][y] = '#'
                                queue.append((x, y))
        return res

grid =[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s= Solution()
print(s.numIslands(grid))