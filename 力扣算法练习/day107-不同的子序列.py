# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day107-不同的子序列
# Author:       xin
# Date:         2019/6/19
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
#
# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
#
# 示例 1:
#
# 输入: S = "rabbbit", T = "rabbit"
# 输出: 3
# 解释:
#
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 示例 2:
#
# 输入: S = "babgbag", T = "bag"
# 输出: 5
# 解释:
#
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        mid_s, set_t = "", set(t)
        for i in range(len(s)):
            if s[i] in set_t:
                mid_s += s[i]
        s = mid_s
        len_s, len_t = len(s), len(t)
        if len_t > len_s:
            return 0
        dp = [[0 for j in range(len_s + 1)] for i in range(len_t + 1)]
        for j in range(len_s + 1):
            dp[0][j] = 1
        for i in range(1, len_t + 1):
            for j in range(1, len_s + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]

s="rabbbit"
t="rabbit"
s1= Solution()
print(s1.numDistinct(s,t))
