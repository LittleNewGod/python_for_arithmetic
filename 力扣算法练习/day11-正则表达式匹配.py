# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 8:45
# @Author  : Xin
# @File    : day11-正则表达式匹配.py
# @Software: PyCharm


# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false


#递归，第一版直接调用
# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#
#         for i in range(len(p)):
#             if p[i] not in '.*' and p[i] not in s:
#                 if i + 1 < len(p) and p[i + 1] != '*' or i + 1 >= len(p):
#                     return False
#         if len(p) < 2:
#             if p == s or (p == '.' and len(s) == 1):
#                 return True
#             else:
#                 return False
#         elif s == '':
#             if p[1] == '*':
#                 if len(p) == 2:
#                     return True
#                 else:
#                     return self.isMatch(s, p[2:])
#             else:
#                 return False
#         elif p[1] == '*':
#             if s[0] == p[0] or p[0] == '.':
#                 if self.isMatch(s[1:], p):
#                     return True
#                 elif self.isMatch(s[1:], p[2:]):
#                     return True
#                 else:
#                     return self.isMatch(s, p[2:])
#             else:
#                 return self.isMatch(s, p[2:])
#         elif s[0] == p[0] or p[0] == '.':
#             return self.isMatch(s[1:], p[1:])
#         else:
#             return False

#递归第二版，封装调用
# 递归（深度优先搜索）
# 一般情况下s和p同时消耗一个字符，若匹配则继续，不匹配则失败；
# 当p中下一个字符是'*'时，p一次消耗两个字符，依次尝试s消耗0，1，2，...个字符进行递归的匹配，若某次结果成功则返回成功。由于s长度有限，这样不会导致无限循环。
class Solution:
    def isMatch(self, s, p):
        return self.match(s, 0, p, 0)

    def match(self, s, i, p, j):
        def check():
            return p[j] == '.' or p[j] == s[i]

        if j == len(p): return i == len(s)

        if j + 1 < len(p) and p[j + 1] == '*':
            # match p[j] 0 - inf times
            if self.match(s, i, p, j + 2):  # 0 match
                return True
            while i < len(s):
                if not check(): return False
                i += 1  # +1 match
                if self.match(s, i, p, j + 2): return True
            else:
                return self.match(s, i, p, j + 2)
        else:
            if i < len(s) and check():
                return self.match(s, i + 1, p, j + 1)
            else:
                return False

#第三版，终极投机取巧直接使用re库，效率也是最快，但存在一个问题，当s,p都是为空的时候re不能使用，会报错
# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         import re
#         re.match()
#         return re.match('^'+p+'$',s)!=None

s = ''
p=''
solution = Solution()
print(solution.isMatch(s,p))
