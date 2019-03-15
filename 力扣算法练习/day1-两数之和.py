# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 18:29
# @Author  : Xin
# @File    : day1-两数之和.py
# @Software: PyCharm


# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        d = {}
        for i, item in enumerate(nums):
            print("i,item",i,item)
            tmp = target - item
            print("tmp",tmp)

            for key, value in d.items():
                print("key,vaule",key,value)
                if value == tmp:
                    print("[key,i]",key,i)
                    return [key, i]

            d[i] = item


        return None



num=[1,5,7,10]
print(enumerate(num))
target = 12
s=Solution()
s.twoSum(num,target)