# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 16:37
# @Author  : Xin
# @File    : day92-打家劫舍.py
# @Software: PyCharm

# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:
#
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l <= 2:
            return max(nums)
        nums1 = nums[:l-1]
        nums2 = nums[1:l]
        ans1 = self.robhelper(nums1)
        ans2=self.robhelper(nums2)
        return max(ans1,ans2)

    def robhelper(self,nums):
        last = 0
        now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

nums = [2,1,1,2]
s = Solution()
print(s.rob(nums))
