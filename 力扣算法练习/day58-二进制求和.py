# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 8:30
# @Author  : Xin
# @File    : day58-二进制求和.py
# @Software: PyCharm

# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"

#解法一：转换为十进制来进行加法，然后转换为二进制
# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(int(a,2)+int(b,2))[2:]
#
#
# a= "11"
# b="1"
# s= Solution()
# print(s.addBinary(a,b))


#解法二：直接二进制进行加法处理，短的串左边补"0", 变成两个数外加进位符逐位相加
class Solution:
    def addBinary(self, a, b):

        s = ""  # 返回值
        carry = 0  # 进位符

        len_max = max(len(a), len(b)) + 1
        a = a.rjust(len_max).replace(' ', '0')
        b = b.rjust(len_max).replace(' ', '0')

        f = lambda x, y, z: int(x) + int(y) + int(z)

        for i in range(len_max - 1, 0, -1):
            c = f(a[i], b[i], carry)
            if c == 0:
                s = '0' + s; carry = 0
            elif c == 1:
                s = '1' + s; carry = 0
            elif c == 2:
                s = '0' + s; carry = 1
            elif c == 3:
                s = '1' + s; carry = 1

        return '1' + s if carry else s

a= "11"
b="1"
s= Solution()
print(s.addBinary(a,b))