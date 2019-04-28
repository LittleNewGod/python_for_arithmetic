# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 9:11
# @Author  : Xin
# @File    : day56-搜索旋转排序数组2.py
# @Software: PyCharm

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
# 示例 2:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
# 进阶:
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

#解法一：内置函数解法
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: bool
#         """
#
#         if target in nums:
#             return True
#         return False
#
# nums=[2,5,6,0,0,1,2]
# target=0
# s=Solution()
# print(s.search(nums,target))


#解法二：二分法
class Solution:
    def search(self, nums, target):
        # return target in nums
        left = 0
        right = len(nums) - 1
        while left <= right:

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2
            # print(left,right,mid)
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

nums=[2,5,6,0,0,1,2]
target=0
s=Solution()
print(s.search(nums,target))

