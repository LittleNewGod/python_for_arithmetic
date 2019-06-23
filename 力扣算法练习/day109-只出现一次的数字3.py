# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day109-只出现一次的数字3
# Author:       xin
# Date:         2019/6/22
# IDE:  PyCharm
# -------------------------------------------------------------------------------


# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
# 注意：
#
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

#解法一：
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans = {}
#         res=[]
#         for i in nums:
#             if i in ans.keys():
#                 ans[i]+=1
#             else:
#                 ans.setdefault(i,1)
#
#         for key,vaule in ans.items():
#             if vaule < 2:
#                 res.append(key)
#         return res
#
# nums=[1, 2, 1, 3, 2, 5]
# s = Solution()
# print(s.singleNumber(nums))

#解法二：思路, 先全部异或一次, 得到的结果, 考察其的某个非0位(比如最高非0位), 那么只出现一次的两个数中, 在这个位上一个为0, 一个为1, 由此可以将数组中的元素分成两部分,重新遍历, 求两个异或值
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         acc = 0
#         for i in nums:
#             acc ^=i
#         n = len(bin(acc))-3
#         a,b=0,0
#         for i in nums:
#             if i>>n&1:
#                 a^=i
#             else:
#                 b^=i
#         return b,a
#
#
# nums=[1, 2, 1, 3, 2, 5]
# s = Solution()
# print(s.singleNumber(nums))

#解法三：优化解法一
class Solution:
    def singleNumber(self, nums):
        mid_set = set()
        for num in nums:
            if num in mid_set:
                mid_set.remove(num)
            else:
                mid_set.add(num)
        return list(mid_set)

nums=[1, 2, 1, 3, 2, 5]
s = Solution()
print(s.singleNumber(nums))