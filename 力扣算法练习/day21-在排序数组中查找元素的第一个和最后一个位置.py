# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 20:51
# @Author  : Xin
# @File    : day21-在排序数组中查找元素的第一个和最后一个位置.py
# @Software: PyCharm

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]

#解法一：无视时间复杂度要求，直接循环求解,时间复杂度为O（n）
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         #nums = [5, 7, 7, 8, 8, 10]
#         ans = []
#         a=0
#         for i in nums:
#             if i ==target:
#                 ans.append(a)
#             a+=1
#         if len(ans)>0:
#             res = [ans[0],ans[-1]]
#             return res
#         return [-1,-1]
#
# nums = [5, 7, 7, 8, 8, 10]
# target=3
# s = Solution()
# print(s.searchRange(nums,target))


#解法二：二分法， 时间复杂度O(log n)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        right = len(nums)-1
        left = 0
        ans = []
        while left <= right:
            mid = (right+left)//2
            if target > nums[mid]:
                left=mid+1
            elif target < nums[mid]:
                right=mid-1
            else:
                for i in range(left,right+1):
                    if nums[i] ==target:
                        ans.append(i)

                break
        if len(ans)>0:
            res = [ans[0],ans[-1]]
            return res
        return [-1,-1]


nums = [5, 7, 7, 8, 8, 10]
target=8
s = Solution()
print(s.searchRange(nums,target))