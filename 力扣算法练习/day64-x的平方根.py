# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 22:22
# @Author  : Xin
# @File    : day64-x的平方根.py
# @Software: PyCharm

# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

#解法一：使用内置函数
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         import math
#         return int(math.sqrt(x))
#
# x = 8
# s = Solution()
# print(s.mySqrt(x))

#解法二：暴力循环
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
             return x
        r = x
        while r > x / r:
             r = (r + x / r) // 2
        return int(r)

x = 8
s = Solution()
print(s.mySqrt(x))

#解法三：暴力循环
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         if x <= 1:
#              return x
#         i =1
#         while i*i <= x:
#              i+=1
#         return i-1
#
# x = 8
# s = Solution()
# print(s.mySqrt(x))


