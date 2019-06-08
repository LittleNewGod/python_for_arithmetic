# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 8:42
# @Author  : Xin
# @File    : day95-柱状图中最大的矩形.py
# @Software: PyCharm

# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# day95-题目图1.png
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
# day95-题目图2.png
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = list()
        heights = [0] + heights + [0]

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[top])

            stack.append(i)

        return res

height = [2,1,5,6,2,3]
s= Solution()
print(s.largestRectangleArea(height))