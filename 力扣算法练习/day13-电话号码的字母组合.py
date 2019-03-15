# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 21:30
# @Author  : Xin
# @File    : day13-电话号码的字母组合.py
# @Software: PyCharm

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

class Solution(object):
    dic_N = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    def letterCombinations(self, digits):
        if digits=='':
            return []
        digits = digits.replace('1','')
        return self.process(digits)
    def process(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        li = []
        if(digits==''):
            return ['']
        else:
            key = digits[0]
            for c in self.dic_N[key]:
                temp = self.process(digits[1:])
                for s in temp:
                    li.append(c+s)
        return li


digits= '234'
s= Solution()
print(s.letterCombinations(digits))
