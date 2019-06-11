# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day99-汇总区间
# Author:       xin
# Date:         2019/6/11
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
#
# 示例 1:
#
# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
# 示例 2:
#
# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

#解法一：一次遍历
# class Solution(object):
#     def summaryRanges(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[str]
#         """
#         if not nums:
#             return nums
#         start, end = nums[0], nums[0]
#         c = []
#         cur = 0
#         while cur < len(nums) - 1:
#             if nums[cur + 1] - nums[cur] == 1:
#                 end = nums[cur + 1]
#                 cur = cur + 1
#             elif start == end:
#                 c.append("{}".format(start))
#                 start = nums[cur + 1]
#                 end = nums[cur + 1]
#                 cur = cur + 1
#             else:
#                 c.append("{}->{}".format(start, end))
#                 start = nums[cur + 1]
#                 end = nums[cur + 1]
#                 cur = cur + 1
#         if nums[cur] - nums[cur - 1] == 1:
#             c.append("{}->{}".format(start, end))
#         if nums[cur] - nums[cur - 1] != 1:
#             c.append("{}".format(nums[cur]))
#         return c
#
#
# nums = [0,1,2,4,5,7]
# s = Solution()
# print(s.summaryRanges(nums))

#解法二：
class Solution(object):
    def summaryRanges(self, nums):
        """
        双指针
        i:遍历到的当前元素
        j:从i开始与前一个元素差为1的最大区间的右边界
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        res = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j] + 1 == nums[j + 1]:
                j += 1
            if j == i:
                res.append(str(nums[i]))
                i += 1
            else:
                res.append(str(nums[i]) + '->' + str(nums[j]))
                i = j + 1
        return res

nums = [0,1,2,4,5,7]
s = Solution()
print(s.summaryRanges(nums))