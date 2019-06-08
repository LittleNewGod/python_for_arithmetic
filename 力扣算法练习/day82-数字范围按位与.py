# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 20:31
# @Author  : Xin
# @File    : day82-数字范围按位与.py
# @Software: PyCharm

# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
#
# 示例 1:
#
# 输入: [5,7]
# 输出: 4
# 示例 2:
#
# 输入: [0,1]
# 输出: 0

#解法一：
# class Solution(object):
#     def rangeBitwiseAnd(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         res = 0
#         ind = 0
#         diff = n - m
#         while m > 0 or n > 0:
#             if m % 2 == 1 and n % 2 == 1:
#                 if 2 ** ind > diff:
#                     res += 2 ** ind
#             m >>= 1
#             n >>= 1
#             ind += 1
#         return res


#解法二：
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = bin(m)[2:]  # 转换为二进制字符串
        b = bin(n)[2:]
        if len(a) != len(b): return 0  # 字符串长度不相等，答案为0
        i = 0
        length = len(a)
        while i < length and a[i] == b[i]:  # 在m和n二进制长度相等的情况下，计算m和n最高位相等 有多少位
            i += 1
        n >>= (length - i)  # 保留最高位相等的二进制
        n <<= (length - i)
        return n

m=5
n=7
s =Solution()
print(s.rangeBitwiseAnd(m,n))