# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 8:34
# @Author  : Xin
# @File    : day61-解码方法.py
# @Software: PyCharm

# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:
#
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

#解法一：动态规划
# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s[0] == "0":
#             return 0
#         now, last = 1, 0
#         s = '99' + s
#         for i in range(2, len(s)):
#             last_count = now
#             add_count = last
#             if int(s[i - 1:i + 1]) > 26:
#                 add_count = 0
#             if s[i] == '0':
#                 add_count = 0
#                 last_count = last
#                 if int(s[i - 1:i + 1]) > 26:
#                     return 0
#             if s[i - 1] == '0':
#                 add_count = 0
#             if s[i - 1:i + 1] == '00':
#                 return 0
#             now, last = last_count + add_count, now
#
#         return now

# s1="101"
# s = Solution()
# print(s.numDecodings(s1))


#解法二：

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if len(s)==0 or s[0]=='0':
#             return 0
#         re_list = [0]*len(s)  # 初始化列表
#         re_list[0] = 1    # 初始化第一个值
#         # 初始化第二个值
#         if len(s)>=2:
#             if '10'<=s[0]+s[1]<='26':
#                 re_list[1] = 1 if s[1]=='0' else 2
#             else:
#                 if s[1]=='0':
#                     return 0
#                 re_list[1] = 1
#         # 剩余的值
#         for i in range(2,len(s)):
#             if '10'<=s[i-1]+s[i]<='26':
#                 re_list[i] = re_list[i - 1] + re_list[i-2]  if s[i] != '0' else re_list[i - 2]
#             else:
#                 if s[i]=='0':
#                     return 0
#                 re_list[i] = re_list[i-1]
#         return re_list[-1]
#
# s1="101"
# s = Solution()
# print(s.numDecodings(s1))


#解法三：有条件的斐波那锲数列

class Solution:
    def numDecodings(self, s: str) -> int:
        v, w, p = 0, int(s>''), ''
        for d in s:
            v=w
            w=(d>'0')*w + (9<int(p+d)<27)*v
            p=d
            #v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w

s1="101"
s = Solution()
print(s.numDecodings(s1))

