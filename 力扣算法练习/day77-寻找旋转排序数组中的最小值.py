# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 13:09
# @Author  : Xin
# @File    : day77-寻找旋转排序数组中的最小值.py
# @Software: PyCharm


# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0

#解法一：直接调用函数找最小值
# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return min(nums)
#
# nums = [3,4,5,1,2]
# s = Solution()
# print(s.findMin(nums))


#解法二：二分法找最小值
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while right>left:
            mid = (right+left)/2
            if nums[mid]>nums[right]:
                if nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                left=mid+1
            else:
                right = mid
        return nums[0]

nums = [3,4,5,1,2]
s = Solution()
print(s.findMin(nums))