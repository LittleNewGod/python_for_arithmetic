# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 21:19
# @Author  : Xin
# @File    : day16-两数相除.py
# @Software: PyCharm

# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 说明:
#
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

#解法-：暴力，但超时了
# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
#         def func(dividend,divisor,ans):
#             if dividend==abs(dividend) and divisor ==abs(divisor):
#
#                 if dividend == divisor:
#                     ans+=1
#                     return ans
#                 elif dividend < divisor:
#                     return 0
#                 while dividend >divisor:
#                     dividend=dividend-divisor
#                     ans+=1
#                 return ans
#
#             elif dividend != abs(dividend) and divisor != abs(divisor):
#                 if dividend == divisor:
#                     ans += 1
#                     return ans
#                 elif dividend > divisor:
#                     return 0
#                 while dividend < divisor:
#                     dividend = dividend - divisor
#                     ans += 1
#                 return ans
#             else:
#                 dividend=abs(dividend)
#                 divisor=abs(divisor)
#                 if dividend == divisor:
#                     ans += 1
#                     return -ans
#                 elif dividend < divisor:
#                     return 0
#                 while dividend > divisor:
#                     dividend = dividend - divisor
#                     ans += 1
#                 return -ans
#
#         if -2**31 < dividend <2**31-1 or -2**31 < divisor < 2**31-1:
#             res = func(dividend, divisor,0)
#             return res
#         return  2**31-1
#
# s = Solution()
# print(s.divide(-10000000000,-3))

#解法二，在解法一下优化
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 1:
            return dividend
        if divisor == -1:
            if -dividend > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return -dividend
        if abs(dividend) < abs(divisor):
            return 0
        flag = 1
        if dividend >= 0 > divisor or dividend <= 0 < divisor:
            flag = -1

        tmpDividend = abs(dividend)
        tmpDivisor = abs(divisor)
        result = 0
        fac = 1
        incDivisor = tmpDivisor

        while tmpDividend >= tmpDivisor:

            if tmpDividend < incDivisor:
                incDivisor = tmpDivisor
                fac = 1
            tmpDividend -= incDivisor
            result += fac
            incDivisor += incDivisor
            fac += fac

        return result * flag

s = Solution()
print(s.divide(-10000000000,-3))

#解法三
#利用位运算符达到快速增减的目的s
# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
#         if dividend == 0:
#             return 0
#         i, res = 0, 0
#         p, q = abs(dividend), abs(divisor)
#         while (q << i) <= p:
#             i += 1
#         for j in range(i-1,-1,-1):
#             if (q << j) <= p:
#                 p -= (q << j)
#                 res += (1 << j)
#         if (dividend ^ divisor) < 0:
#             res = -res
#         return min(res, (1 << 31) - 1)
#
# s = Solution()
# print(s.divide(-10000000000,-3))