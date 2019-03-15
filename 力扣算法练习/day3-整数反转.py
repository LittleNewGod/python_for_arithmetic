# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 18:31
# @Author  : Xin
# @File    : day3-整数反转.py
# @Software: PyCharm


# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        ans=""

        if x_str[0]=='-':
            ans ='-'+x_str[::-1].rstrip('-')
            ans =int(ans)
            return [0,ans][-2**31<ans<2**31-1]

        ans=int(x_str[::-1])
        return [0,ans][-2**31<ans<2**31-1]


x=1534236469
s=Solution()
print(s.reverse(x))