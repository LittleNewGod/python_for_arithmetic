# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 10:13
# @Author  : Xin
# @File    : day51-跳跃游戏2.py
# @Software: PyCharm

# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 说明:
#
# 假设你总是可以到达数组的最后一个位置。

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==1:return 0
        reach = 0
        nextreach = nums[0]
        step = 0
        for i in range(len(nums)):
            nextreach = max(i+nums[i],nextreach)
            if nextreach >= len(nums)-1:
                return step+1
            if i == reach:
                step += 1
                reach = nextreach
        return step

nums = [2,1,1,1,4]
s = Solution()
print(s.jump(nums))