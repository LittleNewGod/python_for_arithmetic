# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day101-最大矩形
# Author:       xin
# Date:         2019/6/13
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
#
# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6

#解法一：二进制
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in matrix]
        ans, N = 0, len(nums)
        for i in range(N):
            j, num = i, nums[i]
            while j < N:
                num = num & nums[j]
                if not num:
                    break
                l, curnum = 0, num
                while curnum:
                    l += 1
                    curnum = curnum & (curnum << 1)
                ans = max(ans, l * (j - i + 1))
                j += 1
        return ans

matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s = Solution()
print(s.maximalRectangle(matrix))


#解法二：
# class Solution(object):
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         if not matrix or not matrix[0]:
#             return 0
#         res = 0
#         n = len(matrix[0])
#         heights = [0] * (n + 1)
#         for row in matrix:
#             for i in range(n):
#                 heights[i] = heights[i] + 1 if row[i] == '1' else 0
#             s = []
#             for i in range(len(heights)):
#                 # 当前位置小于栈顶位置时计算
#                 while s and heights[s[-1]] > heights[i]:
#                     h = heights[s.pop()]
#                     # i-s[-1]-1 和 i 是底
#                     area = h * (i - s[-1] - 1 if s else i)
#                     res = max(res, area)
#                 s.append(i)
#         return res
#
# matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# s = Solution()
# print(s.maximalRectangle(matrix))



