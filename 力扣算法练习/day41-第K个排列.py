# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 21:31
# @Author  : Xin
# @File    : day41-第K个排列.py
# @Software: PyCharm

# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"


#解析：
# 以n=4,k=17为例吧. 4位数排列一共有4!=24种排列方式. 其中在千位上每个数字出现3!次,在百位上每个数字出现2!次,十位上每个数字出现1!次,个位上每个数字出现0!次. 因为需要多次计算阶乘,所以使用了一个辅助函数.
# 因为索引的时候是从0开始,所以k=17,我们索引的时候即为16.
# 对于千位上的数字,因为16//3! = 2,所以第一个数字即为nums[2],也就是3.此时我们确定了要求的数字落在了以3开头的数字上.此时把 nums = '12456789' 此时需要决定百位上的数字.我们要取的数字是形如'3xxx'的第几个呢? 更新k =k%3! 此时k=4,也就是'3xxx'中的第四个数字.又因为在百位数上,每个数字都出现了2!次,所以k//2!=2. 第二个数字为nums[2],也就是4.此时我们确定要选的数字为'34xx'.
# 然后依次类推,按照取余决定k,整除确定具体的pos,然后决定最终要选的数字即可.

#解法一：
# class Solution(object):
#     def getPermutation(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#         output = ''
#         nums = '123456789'
#         k -= 1
#
#         while n >= 1:
#             index = self.permutation(n - 1)
#             pos = k // index
#             k %= index
#             output += nums[pos]
#             nums = nums[:pos] + nums[pos + 1:]
#             n -= 1
#
#         return output
#
#     def permutation(self, n):
#         if n == 1 or n == 0:
#             return 1
#         else:
#             return n * self.permutation(n - 1)
#
#
# n=3
# k=4
# s=Solution()
# print(s.getPermutation(n,k))

#解法二：
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"
        k -= 1
        tmp = [i+1 for i in range(n)]
        tmp1 = [0 for i in range(n+1)]
        tmp1[0] = 1
        for i in range(1,len(tmp1)):
            tmp1[i] = tmp1[i-1]*i
        s = ""
        while tmp:
            a = k % tmp1[len(tmp)-1]
            b = k // tmp1[len(tmp)-1]
            s += str(tmp[b])
            tmp.pop(b)
            k = a
        return s

n=3
k=4
s=Solution()
print(s.getPermutation(n,k))
