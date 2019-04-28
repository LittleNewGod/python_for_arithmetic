# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 6:41
# @Author  : Xin
# @File    : day53-子集.py
# @Software: PyCharm

# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

#解法一：利用itertools模块函数生成子序列，效率最高
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        ans = []
        for i in range(len(nums)):
            temp = itertools.combinations(nums,i)
            for i in temp:
                ans.append(list(i))
        return ans

nums = [1,2,3]
s = Solution()
print(s.subsets(nums))


#解法二：位运算
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         half = [[]]
#         for i in range(len(nums)):
#             for j in range(1 << i):
#                 newSub = half[j][:]
#                 newSub.append(nums[i])
#                 half.append(newSub)
#         full = half
#         return full
#
# nums = [1,2,3]
# s = Solution()
# print(s.subsets(nums))


#解法三：递归回溯法
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ans = []
#         def dfs(lst, nums, pos):
#             ans.append(lst[:])
#             for i in range(pos, len(nums)):
#                 lst.append(nums[i])
#                 dfs(lst, nums, i + 1)
#                 lst.pop()
#         dfs([], nums, 0)
#         return ans
#
# nums = [1,2,3]
# s = Solution()
# print(s.subsets(nums))