# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 10:24
# @Author  : Xin
# @File    : day47-字符串相乘.py
# @Software: PyCharm

# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         return str(int(num1)*int(num2))
#
# num1=3
# num2=7
# s = Solution()
# print(s.multiply(num1,num2))

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #数字倒过来，因为计算的时候从最低位迭代
        num1=num1[::-1]
        num2=num2[::-1]
        #创建空列表99*99不超过10000，也就是n位数*m位数不会超过，n+m+1
        LIST = [0] * (len(num1) + len(num2)+1)
        #str_to_int是一个通过ASCII码转化int到str的自制函数，但他只能计算十以内的乘法
        #所以将每一位计算
        for i in range(len(num1)):
            for j in range(len(num2)):
                LIST[j+i]+=self.str_to_int(num1[i])*self.str_to_int(num2[j])
        #将本位和进位分别计算然后统一处理
        for i in range(len(LIST)-1):
            INDEX= LIST[i]//10
            LIST[i]=LIST[i]%10
            LIST[i+1]+=INDEX
        #将计算的结果转化成字符串
        res=''
        for i in LIST:
            res+=str(i)
        res=res[::-1].lstrip('0')
        if res:
            return res
        else:
            return '0'


    def str_to_int(self,num1):
        return ord(num1)-ord('0')

num1='3'
num2='7'
s = Solution()
print(s.multiply(num1,num2))