# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day110-丑数2
# Author:       xin
# Date:         2019/6/23
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  
#
# 1 是丑数。
# n 不超过1690。

#解法：三指针
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(n - 1):
            res.append(min(res[idx2] * 2, res[idx3] * 3, res[idx5] * 5))
            if res[-1] == res[idx2] * 2:
                idx2 += 1
            if res[-1] == res[idx3] * 3:
                idx3 += 1
            if res[-1] == res[idx5] * 5:
                idx5 += 1
        return res[-1]

