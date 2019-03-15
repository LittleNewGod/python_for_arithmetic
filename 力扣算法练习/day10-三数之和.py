# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 21:47
# @Author  : Xin
# @File    : day10-三数之和.py
# @Software: PyCharm


# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #先将列表排序
        nums.sort()
        #创建空列表用来储存结果
        res = []
        i = 0
        #循环列表
        for i in range(len(nums)):
            #先固定一个数，然后使用双指针
            if i == 0 or nums[i]>nums[i-1]:
                l=i+1
                r = len(nums)-1
                while l <r:
                    #计算三数之和
                    s = nums[i]+nums[l]+nums[r]
                    #当和为0就存入结果列表，并且左右指针同时推进一位
                    if s == 0:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1
                        #下面两个循环是防止邻近的两数相等，造成生成相同的结果集
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    #当和大于0则右指针向左推进一位
                    elif s>0:
                        r-=1
                    #当和小于0则左指针向右推进一位
                    else:
                        l+=1

        return res

nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))