# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 8:59
# @Author  : Xin
# @File    : day45-通配符匹配.py
# @Software: PyCharm

# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
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
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[bool(0) for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = bool(1)
        # 开始初始化填充,如果匹配的串s是空的的话，只有模式是*才能匹配
        for i in range(n):
            if dp[0][i] and p[i] == '*':
                dp[0][i + 1] = bool(1)

        ## 开始动态规划
        for i in range(m):
            for j in range(n):
                if p[j] == '*':
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]
                elif p[j] == '?' or s[i] == p[j]:
                    dp[i + 1][j + 1] = dp[i][j]
        print(dp)
        return dp[m][n]


st = 'adceb'
p ='a*b'
s = Solution()
print(s.isMatch(st,p))