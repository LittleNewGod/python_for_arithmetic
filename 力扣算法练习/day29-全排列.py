# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 20:51
# @Author  : Xin
# @File    : day29-全排列.py
# @Software: PyCharm

# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #nums = [1, 2, 3]
        if nums is None:return []
        if len(nums)==1:return [nums]
        res = []
        for x in nums:
            temp = nums+[]#加个空列表是必须的，这个类似的意思就是深拷贝一个列表，这样使用remove不会影响到原列表数据
            temp.remove(x)
            for y in self.permute(temp):
                res.append([x]+y)
        return res


nums = [1,2,3]
s = Solution()
print(s.permute(nums))

