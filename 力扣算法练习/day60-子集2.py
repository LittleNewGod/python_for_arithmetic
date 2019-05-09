# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 9:24
# @Author  : Xin
# @File    : day60-子集2.py
# @Software: PyCharm

# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution(object):
    def __init__(self):
        self.res = []
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #先排序
        nums.sort()
        self.dfs([], 0, nums)
        return self.res
    def dfs(self, temp, j, nums):
        self.res.append(temp[:])
        for i in range(j, len(nums)):
            #跳过重复
            if i > j and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.dfs(temp, i+1, nums)
            temp.pop()
        return

nums= [4,4,4,1,4]
s = Solution()
print(s.subsetsWithDup(nums))
