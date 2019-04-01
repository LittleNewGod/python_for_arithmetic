# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 21:28
# @Author  : Xin
# @File    : day28补-实现strStr().py
# @Software: PyCharm

# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。



#解法一：投机取巧法，使用内置函数
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         import re
#         if len(needle)==0:
#             return 0
#         if haystack.__contains__(needle):
#             return haystack.index(needle)
#             # a = re.search(needle,haystack)
#             # return a.start(0)
#
#         return -1
#
#
#
#
#
#
# haystack = 'hello'
# needle = 'll'
# s= Solution()
# print(s.strStr(haystack,needle))


#解法二：暴力循环
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j <len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                i = i - j + 1
                j = 0
        if j == len(needle):
            return i - j
        return -1


haystack = 'aaaaa'
needle = 'aab'
s= Solution()
print(s.strStr(haystack,needle))
