# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 18:08
# @Author  : Xin
# @File    : day84-编辑距离.py
# @Software: PyCharm


# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')


#解法一：
# class Solution(object):
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         len1 = len(word1)
#         len2 = len(word2)
#         '''
#         动态规划
#         step1: 状态
#         首先只定义一维 DP[i] 不能有效简化问题的处理
#         使用 二维 DP[i][j]，表示 word1 的 i 个字母 与 word2 的 第 j 个字母 相同 需要的操作步骤数
#         将最对 word1 处理 转化为 对 word1 和 word2 均处理
#         word1 插入一个字符   DP[i-1][j] + 1 ->  DP[i][j]
#         word1 删除一个字符 = word2 插入一个字符  DP[i][j-1] + 1 -> DP[i][j]
#         word1 替换一个字符 = word1 word2 都替换一个字符 DP[i-1][j-1] + 1 -> DP[i][j]
#         step2: 动态方程
#         DP[i][j]  A、 word1 的 i 个字母 与 word2 的 第 j 个字母 相同
#                      DP[i][j] =  DP[i-1][j-1]  #不操作
#                   B、不相同,需要进行 插入 删除 或者 替换操作
#                      DP[i][j]  =  min(DP[i-1][j] + 1,DP[i][j-1] + 1,DP[i-1][j-1]+1)
#
#         '''
#         DP = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
#         # 初始
#         for i in range(len1 + 1):
#             DP[i][0] = i
#         for j in range(len2 + 1):
#             DP[0][j] = j
#         for i in range(1, len1 + 1):
#             for j in range(1, len2 + 1):
#                 if word1[i - 1] == word2[j - 1]:
#                     DP[i][j] = DP[i - 1][j - 1]
#                 else:
#                     DP[i][j] = min(DP[i - 1][j] + 1, DP[i][j - 1] + 1, DP[i - 1][j - 1] + 1)
#         return DP[len1][len2]


# word1="horse"
# word2="ros"
# s= Solution()
# print(s.minDistance(word1,word2))



#解法二：
class Solution(object):
    def minDistance(self, word1, word2):
        """

        """
        res = 0
        if word1==word2: return 0
        n = len(word1)
        m = len(word2)
        f = [[0 for j in range(m+1)] for i in range(n+1)]
        for j in range(m+1):
            f[0][j] = j
        for i in range(n+1):
            f[i][0] = i
        def dfs(i, j):
            if i==1 and j==1:
                f[1][1] = 0 if word1[i-1] == word2[j-1] else 1
                return f[1][1]
            if f[i][j] !=0: return f[i][j]
            if word1[i-1] == word2[j-1]:
                f[i][j] = dfs(i-1, j-1)
            else:
                f[i][j] = 1+min(dfs(i-1, j), dfs(i, j-1), dfs(i-1,j-1))
            return f[i][j]
        return dfs(n, m)

word1="horse"
word2="ros"
s= Solution()
print(s.minDistance(word1,word2))
