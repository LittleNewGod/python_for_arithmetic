# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 18:32
# @Author  : Xin
# @File    : day4-最长回文子串.py
# @Software: PyCharm

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = ""
        for i in range(2*len(s)-1):
            if i%2 == 0:
                start = end = i//2
                while start>=0 and end<len(s) and s[start]==s[end]:
                    start-=1
                    end+=1
            else:
                start = (i-1) // 2
                end = (i+1) //2
                while start>=0 and end<len(s) and s[start]==s[end]:
                    start-=1
                    end+=1
            if len(str)<=(end-start-1):
                str=s[start+1:end]
        return str


s='baced'
so=Solution()
print(so.longestPalindrome(s))