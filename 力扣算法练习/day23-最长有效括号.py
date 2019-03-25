# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 23:11
# @Author  : Xin
# @File    : day23-最长有效括号.py
# @Software: PyCharm

# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"


# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         st, b = [], [0] * len(s)
#         for i, val in enumerate(s):
#             if val == '(':
#                 st.append(i)
#             elif st:
#                 b[st.pop()], b[i] = 1, 1
#
#         c, mc = 0, 0
#         for i in b:
#             if i:
#                 c += 1
#             else:
#                 mc = max(c, mc)
#                 c = 0
#
#         return max(c, mc)
# temp="()(()"
# s = Solution()
# print(s.longestValidParentheses(temp))


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ')' + s
        r1 = [')',]
        r2 = [0,]
        for i in s[1:] :
            if i == '(':
                r1.append('(')
                r2.append(0)
            else:
                if r1[-1] == '(':
                    del r1[-1]
                    r2[-2] += (2 + r2[-1])
                    del r2[-1]
                else:
                    r1.append(')')
                    r2.append(0)
        return max(r2)

temp="()(()"
s = Solution()
print(s.longestValidParentheses(temp))
