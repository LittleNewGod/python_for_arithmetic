# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 9:23
# @Author  : Xin
# @File    : day46-最大子序和.py
# @Software: PyCharm

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

#写法二：
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums =[-2,-1,-3]
#         res = nums[0]
#         ans = 0
#         for i in nums:
#             if ans >0:
#                 ans += i
#             else:
#                 ans = i
#             res = max(res,ans)
#         return res
#
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# s=Solution()
# print(s.maxSubArray(nums))

#写法一：DP
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)

nums=[-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
print(s.maxSubArray(nums))
