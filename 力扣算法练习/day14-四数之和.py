# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 20:31
# @Author  : Xin
# @File    : day14-四数之和.py
# @Software: PyCharm

# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans =[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums)-1
                while l<r:
                   temp = nums[i]+nums[j]+nums[l]+nums[r]
                   if temp==target:
                       arr = [nums[i],nums[j],nums[l],nums[r]]
                       if arr not in ans:
                           ans.append([nums[i],nums[j],nums[l],nums[r]])
                       l+=1
                       r-=1
                       while l<r and nums[l]==nums[l-1]:
                           l+=1
                       while l<r and nums[r]==nums[r+1]:
                           r-=1
                   elif temp<target:
                       l+=1
                   else:
                       r-=1

        return ans


nums = [-3,-2,-1,0,0,1,2,3]
target = 0
s = Solution()
print(s.fourSum(nums,target))
