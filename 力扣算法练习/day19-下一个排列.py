# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 9:23
# @Author  : Xin
# @File    : day19-下一个排列.py
# @Software: PyCharm

# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


#解法一：
# 定义了两个辅助函数,互换(swap)和序列逆转(reverse). 觉得这种方法很好.有一点双指针的意思
#
# 用nums = [1,3,5,7,6,4,2,1]来做示范吧. 首先,第一个指针从队尾开始向前遍历(i = len(nums) - 2),判断一下i+1与i的大小关系.在遍历到5之前,一直是nums[i]>nums[i+1]. 在第一个指针指向5时,第二个指针同样从队尾出发,因为在逆向遍历到i之前,一直是升序的,刚开始nums[j] <= nums[i]是一直满足的,当j停止移动时,j指向的数字是刚刚好大于nums[i]的,在例子中,j刚好指向6.
#
# 将nums[i]与nums[j]进行互换.此时nums = [1,3,6,7,5,4,2,1].此时6之后的数字是降序的,所以将6之后数字进行反转,才能达到题目要求"刚好大于原序列的效果",然后将nums[i+1:]进行反转即可.
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= i and nums[j] <= nums[i]:
                j -=1
            self.swap(nums,i,j)
        self.reverse(nums,i+1)

    def reverse(self,nums,start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums,i,j)
            i+=1
            j-=1

    #互换数字
    def swap(self,nums,i,j):
        # temp = nums[i]
        # nums[i]= nums[j]
        # nums[j]=temp
        nums[i],nums[j] = nums[j],nums[i]

nums = [1,3,5,7,6,4,2,1]
#nums=[1,2,3]
s = Solution()
s.nextPermutation(nums)
print(nums)


#解法二：
# 从末尾(i)开始检查相邻两个元素(i和i-1)，是否是逆序对（nums[i-1] < nums[i]）
# 如果出现后面的(i)比前面(i-1)大，说明如果交换，可以使整体变大，但此时的交换未必带来最接近的大值
# 因为我们不知道i是不是最接近i-1的大值，只有是最接近的交换才能带来最接近nums的大值
# 所以，从i开始向结尾寻找最接近i-1的大值，找到之后，和i-1交换
# 然后还要对i到结尾的所有元素进行从小到大的排列，以此保证新的nums在进行交换后的进一步缩小
# 最后，此时的nums是最接近初值的大值。
# class Solution:
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         flag = False
#         if len(nums) > 1:
#             i = len(nums) - 1
#             while i > 0:
#                 if nums[i] > nums[i - 1]:
#                     index = i
#                     for j in range(i + 1, len(nums)):
#
#                         if nums[i - 1] < nums[j] and nums[j] < nums[index]:
#                             index = j
#                     nums[index], nums[i - 1] = nums[i - 1], nums[index]
#                     temp = nums[i:]
#                     temp.sort()
#                     for v in temp:
#                         nums[i] = v
#                         i += 1
#                     flag = True
#                     break
#                 else:
#                     i -= 1
#         if not flag:
#             nums.reverse()


# #nums = [1,3,5,7,6,4,2,1]
# nums=[1,2,3]
# s = Solution()
# s.nextPermutation(nums)
# print(nums)
