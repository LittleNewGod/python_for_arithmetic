# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 15:35
# @Author  : Xin
# @File    : day87-长度最小的子数组.py
# @Software: PyCharm


# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 进阶:
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

#解法一：
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = len(nums) + 1
        j = -1
        su = 0
        for i in range(len(nums)):
            su += nums[i]
            while su >= s:
                res = min(res, i - j)
                j += 1
                su -= nums[j]
        return 0 if res == len(nums) + 1 else res

nums = [1,2,3,4,5]
p = 11
s = Solution()
print(s.minSubArrayLen(p,nums))

