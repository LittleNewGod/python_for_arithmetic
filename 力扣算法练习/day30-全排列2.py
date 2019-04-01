# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 22:14
# @Author  : Xin
# @File    : day30-全排列2.py
# @Software: PyCharm

# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

#解法一，其实day29的一样，就加多了一个去重判断，效率有点慢
# class Solution(object):
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if nums is None:return []
#         if len(nums) == 1:return [nums]
#         res = []
#         for x in nums:
#             temp = nums+[]
#             temp.remove(x)
#             for y in self.permuteUnique(temp):
#                 if not res.__contains__([x]+y):
#                     res.append([x]+y)
#         return res
#
# nums = [1,1,2]
# s = Solution()
# print(s.permuteUnique(nums))

#解法二：
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        X = []
        def tree(li, k, length):
            if k==length:
                X.append(li[:])
            else:
                for i in range(k,length):
                    if nums[i] in nums[k:i]:
                        continue
                    li[k], li[i] = li[i], li[k]
                    tree(li, k+1, length)
                    li[i], li[k] = li[k], li[i]
        tree(nums, 0, len(nums))
        # print(X)
        return X

nums = [1,1,2]
s = Solution()
print(s.permuteUnique(nums))
