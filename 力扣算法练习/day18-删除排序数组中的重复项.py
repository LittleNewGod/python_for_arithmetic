# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 10:13
# @Author  : Xin
# @File    : day18-删除排序数组中的重复项.py
# @Software: PyCharm


# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定数组 nums = [1,1,2],
#
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

#解法-：暴力法，直接循环列表，操作列表
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i =1
#         j =len(nums)
#         if j <= 1:
#             return j
#         while i<j :
#             if nums[i]==nums[i-1]:
#                 #因为不能使用额外的空间，所以想到的是直接操作列表，pop或remove,亲测使用pop的效率更高
#                 #nums.pop(i)
#                 nums.remove(nums[i])
#                 j -= 1
#             else:
#                 i+=1
#
#         return len(nums)
#
# nums=[2,2,2,3,4]
# s = Solution()
# print(s.removeDuplicates(nums))


#解法二：此方法其实有点不符合原题，虽然返回的不重复整数个数，但没有删除列表重复数字，
#但如果也是一种思路，在没有改变列表长度的情况下返回列表不重复数字个数
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mylen = len(nums)
        if mylen <= 1:
            return mylen
        p = 0
        for tem in nums:
            if nums[p] != tem:
                nums[p + 1] = tem
                p += 1
        return p+1


nums=[2,2,2,3,4]
s = Solution()
print(s.removeDuplicates(nums))