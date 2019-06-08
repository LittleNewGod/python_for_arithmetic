# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 20:44
# @Author  : Xin
# @File    : day94-存在重复元素3.py
# @Software: PyCharm


# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool

        滑动窗口
        i:遍历到的当前数
        j:与i绝对值只差>t且离i最近的数的索引
        对nums带上索引一起预排序
        时间复杂度O(n^2),对k很大,j很小的测试数据非常友好
        """

        n = len(nums)
        nums = sorted([(nums[i], i) for i in range(n)], key=lambda x: x[0])
        j = 0
        for i in range(n):
            while j < i and nums[j][0] + t < nums[i][0]:
                j += 1
            if any(abs(nums[i][1] - nums[x][1]) <= k for x in range(j, i)):
                return True
        return False

nums = [1,2,3,1]
k = 3
t = 0
s = Solution()
print(s.containsNearbyAlmostDuplicate(nums,k,t))