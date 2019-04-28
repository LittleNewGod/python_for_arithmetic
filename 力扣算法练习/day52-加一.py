# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 9:13
# @Author  : Xin
# @File    : day52-加一.py
# @Software: PyCharm


# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

#解法一：取数组最后一个数字相加即可，注意进位相加的判断就行
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #digits=[1]
        l = len(digits)-1
        if l==0:
            if digits[l]==9:return [1,0]
            digits[l]+=1
            return digits
        while l>0:
            if digits[l] != 9:
                digits[l]+=1
                return digits
            elif digits[l]==9 and digits[l-1]!=9:
                digits[l]=0
                digits[l-1]+=1
                return digits
            else:
                if l-1==0:
                    digits[l]=0
                    digits[l-1]=0
                    digits.insert(0,1)
                    return digits

                digits[l]=0
                l-=1

digits = [1,9]
s = Solution()
print(s.plusOne(digits))


#解法二：转换整个列表成一个完整数字再相加，然后再转换为列表，此效率较慢，但写法简单

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_digits = [str(x) for x in digits]
        ans = str(int(''.join(new_digits))+1)
        res=[]
        for i in ans:
            res.append(int(i))
        return res



digits = [1,9]
s = Solution()
print(s.plusOne(digits))