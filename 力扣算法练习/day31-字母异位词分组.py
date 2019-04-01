# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 12:42
# @Author  : Xin
# @File    : day31-字母异位词分组.py
# @Software: PyCharm


# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

#解法一：使用字典键唯一的特性去重，这个解法有两种写法，一个是使用原生dict，然后使用setdefault为字典记值，另一个是使用collections包的defaultdict，使用collecttions的效率更快
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = collections.defaultdict(list)
        #ans = dict()
        for s in strs:
            ans[tuple(sorted(s))].append(s)
            #ans.setdefault(tuple(sorted(s)),[]).append(s)
        return ans.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s=Solution()
print(s.groupAnagrams(strs))