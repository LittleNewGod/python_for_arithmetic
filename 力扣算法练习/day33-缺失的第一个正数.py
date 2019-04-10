# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 9:12
# @Author  : Xin
# @File    : day33-缺失的第一个正数.py
# @Software: PyCharm

# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 说明:
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

#写法一：先创建相等长度一个正数的列表，由小到大判断是否在存在题参中，当出现不存在就返回，先排序一下能减少循环次数
# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         l = len(nums)+2
#         if len(nums)==0:
#             return 1
#         for i in range(1,l):
#             if i in nums:
#                 pass
#             else:
#                 return i
#
# nums = [3,4,-1,1]
# s = Solution()
# print(s.firstMissingPositive(nums))

#写法二：利用字典来排除
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return 1
        nums.sort()
        mydict = dict()
        res =1
        for i in nums:
            mydict[i]=1
        while mydict.__contains__(res):
            res+=1
        return res


nums = [3,4,-1,1]
s = Solution()
print(s.firstMissingPositive(nums))