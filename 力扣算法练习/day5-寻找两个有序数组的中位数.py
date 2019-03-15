# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 18:34
# @Author  : Xin
# @File    : day5-寻找两个有序数组的中位数.py
# @Software: PyCharm


# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1+nums2
        nums.sort()
        #列表个数为偶数
        if(len(nums)%2==0):
            mid =len(nums)//2
            ans = (nums[mid-1]+nums[mid])/2
            return ans
        #列表个数为奇数
        if(len(nums)%2!=0):
            mid = (len(nums)+1)//2
            ans = nums[mid-1]
            return ans


num1=[-1,-2,-6,7]
num2=[3,4]
s =Solution()
print(s.findMedianSortedArrays(num1,num2))
