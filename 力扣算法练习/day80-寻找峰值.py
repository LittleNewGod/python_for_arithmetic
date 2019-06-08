# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 11:49
# @Author  : Xin
# @File    : day80-寻找峰值.py
# @Software: PyCharm

# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
# 说明:
#
# 你的解法应该是 O(logN) 时间复杂度的。

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:return 1

        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1

nums = [1,2,1,3,5,6,4]
s =Solution()
print(s.findPeakElement(nums))

