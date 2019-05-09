# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 18:17
# @Author  : Xin
# @File    : day67-插入区间.py
# @Software: PyCharm

# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

#解法一：
# class Solution(object):
#     def insert(self, intervals, newInterval):
#         """
#         :type intervals: List[List[int]]
#         :type newInterval: List[int]
#         :rtype: List[List[int]]
#         """
#         i=0
#         flag=0
#         intervals.append(newInterval)
#         l=sorted(intervals,key=lambda x:x[0])
#         while i < len(l)-1:
#             if l[i][1]>=l[i+1][0]:
#                 l[i]=[l[i][0],max(l[i][1],l[i+1][1])]
#                 l.remove(l[i+1])
#                 flag=1
#             else:
#                 if flag:break
#                 i+=1
#         return l

# intervals= [[1,3],[6,9]]
# newInterval = [2,5]
# s = Solution()
# print(s.insert(intervals,newInterval))

#解法二：二分查找
class Solution:
    def binarySerach(self, arr, key, is_left):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][is_left] >= key if is_left else arr[mid][is_left] > key:
                right = mid - 1
            else:
                left = mid + 1
        return left if is_left else left - 1

    def insert(self, intervals, newInterval):
        left_index = self.binarySerach(intervals, newInterval[0], 1)
        right_index = self.binarySerach(intervals, newInterval[1], 0)
        if left_index == len(intervals):
            intervals.append(newInterval)
        elif right_index == -1:
            intervals.insert(0, newInterval)
        else:
            intervals[left_index:right_index + 1] = [
                [min(intervals[left_index][0], newInterval[0]), max(intervals[right_index][1], newInterval[1])]]
        return intervals

intervals= [[1,3],[6,9]]
newInterval = [2,5]
s = Solution()
print(s.insert(intervals,newInterval))