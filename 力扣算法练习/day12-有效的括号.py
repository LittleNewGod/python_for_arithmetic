# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 21:27
# @Author  : Xin
# @File    : day12-有效的括号.py
# @Software: PyCharm

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true

#解法-：用栈弹出元素
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         keys = {"(": ")", "[": "]", "{": "}"}
#         stack = list()
#         for i in range(len(s)):
#             if s[i] in keys:
#                 stack.append(s[i])
#             else:
#                 if len(stack) == 0:
#                     return False
#                 if keys[stack.pop()] != s[i]:
#                     return False
#         if len(stack) != 0:
#             return False
#         return True

#解法二：因为假如字符串可能为真的情况，那么必然最少都有一对完整闭合的括号，所以可以利用消除来处理
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

str= "{([])()}"
s = Solution()
print(s.isValid(str))
