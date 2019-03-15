# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 21:19
# @Author  : Xin
# @File    : day15-括号生成.py
# @Software: PyCharm

# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res =[]
        self.generate(res,'',0,0,n)
        return res

    def generate(self,res,ans,count1,count2,n):
        if count1>n or count2>n: return
        if count1==n and count2==n: res.append(ans)
        if count1 >= count2:
            ans1=ans
            self.generate(res, ans+'(', count1+1, count2, n)
            self.generate(res, ans1+')', count1, count2+1, n)


n = 3
s=Solution()
print(s.generateParenthesis(n))