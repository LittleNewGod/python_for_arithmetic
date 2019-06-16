# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day104-除自身以外数组的乘积
# Author:       xin
# Date:         2019/6/16
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

#解法一：两层for循环，进行连乘，中间判断一下i != j 即可。时间复杂度O(n^2)，ps:这样是分超时的
# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         ans = [1 for i in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if i != j:
#                     ans[i]*=nums[j]
#         return ans
#
# nums=[1,2,3,4]
# s= Solution()
# print(s.productExceptSelf(nums))


#解法二：时间复杂度O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        B = [1 for i in range(n)]
        for i in range(1,n):
            B[i] = B[i-1] * nums[i-1]
        tmp = 1
        for i in range(n-2,-1,-1):
            tmp *= nums[i+1]
            B[i] *= tmp
        return B

nums=[1,2,3,4]
s= Solution()
print(s.productExceptSelf(nums))