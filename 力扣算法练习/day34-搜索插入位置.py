# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 13:04
# @Author  : Xin
# @File    : day34-搜索插入位置.py
# @Software: PyCharm

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0

#解法一：暴力循环列表，没有任何技巧，效率较慢
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if target<=nums[0]:return 0
#         if target>nums[len(nums)-1]:return len(nums)
#         if target == nums[len(nums) - 1]: return len(nums)-1
#         for i in range(len(nums)):
#             if target>=nums[i-1] and target<nums[i]:
#                 return i
#
# nums = [1,2,5]
# target = 3
# s = Solution()
# print(s.searchInsert(nums,target))


#解法二：二分法
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if target<=nums[0]:return 0
#         if target>nums[len(nums)-1]:return len(nums)
#         if target == nums[len(nums) - 1]: return len(nums)-1
#
#         l = 0
#         r = len(nums)
#         while l<r:
#             mid =(r+l)//2
#             if target==nums[mid]:
#                 return mid
#             elif target>nums[mid]:
#                 l = mid+1
#             elif target<nums[mid]:
#                 r = mid
#         return l
#
#
#
# nums = [1,3,5,6]
# target = 2
# s = Solution()
# print(s.searchInsert(nums,target))

#解法三：使用内置函数
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)



nums = [1,3,5,6]
target = 2
s = Solution()
print(s.searchInsert(nums,target))

