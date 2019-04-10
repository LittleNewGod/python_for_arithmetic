# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 17:08
# @Author  : Xin
# @File    : day37-合并区间.py
# @Software: PyCharm

# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

#本题主要是注意，pop之后数组变了，但是只要用 while,就是会一直在原来的位置一直合并，直到最后合并不了了，再下一个index
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return []
        i=0
        intervals.sort(key=lambda x:(x.start,x.end))
        while i<len(intervals)-1:
            while i+1<len(intervals) and intervals[i].end>=intervals[i+1].start:
                intervals[i].end=max(intervals[i].end,intervals[i+1].end)
                intervals.pop(i+1)
            i+=1
        return intervals

#i = Interval(0,18)
intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(Interval))
