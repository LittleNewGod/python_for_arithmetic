# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day98-基本计算器2
# Author:       xin
# Date:         2019/6/10
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1:
#
# 输入: "3+2*2"
# 输出: 7
# 示例 2:
#
# 输入: " 3/2 "
# 输出: 1
# 示例 3:
#
# 输入: " 3+5 / 2 "
# 输出: 5
# 说明：
#
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.replace(' ','')
        num,tmp='',[]
        for k in range(len(s)):   #分离数值和运算符，存入tmp
            if s[k] in '0123456789':
                num+=s[k]
            else:
                tmp.append(int(num))
                tmp.append(s[k])
                num=''
        tmp.append(int(num))
        if len(tmp)==1:
            return tmp[0]

        stack,i=[],0  #初始栈
        while i<len(tmp):
            stack.append(tmp[i])   #入栈
            if tmp[i]=='*' or tmp[i]=='/':
                v=stack[-2]*tmp[i+1] if tmp[i]=='*' else stack[-2]//tmp[i+1]
                stack.pop()   #  当前'*/'符号，上一个数字 出栈
                stack.pop()
                stack.append(v)   #乘除结果入栈
                i+=1
            i+=1
        #现在栈里只有加减法了
        res=int(stack[0])
        if len(stack)==1:
            return res
        i=1
        while i<len(stack)-1:
            if stack[i]=='+' or stack[i]=='-':
                res=res+stack[i+1] if stack[i]=='+' else res-stack[i+1]
                i+=1
            i+=1
        return res

s1 = "3+2*2"
s = Solution()
print(s.calculate(s1))
