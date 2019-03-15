# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 21:33
# @Author  : Xin
# @File    : day7-两数相加.py
# @Software: PyCharm

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

'''
以下第一版代码本地运行没问题，但提交出错，因为这里的参数限定是自创链表迭代器，而不是python本身的列表。
改进方法需要先实例那个迭代器对象，next()来获取链表的值相加，第二版代码是参考别人的。
'''
#第一版：
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        for i in range(len(l1)):
            num1 += l1[i] * 10 ** i
        for i in range(len(l2)):
            num2 += l2[i] * 10 ** i

        num3 = num1 + num2

        str_num = str(num3)[::-1]
        num = []
        for i in str_num:
            num.append(int(i))

        return num


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#第二版
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         tmpnode = ListNode(0)  # 第一个节点需要舍弃
#         res = tmpnode  # 返回值
#         add = 0  # 进位
#         while l1 or l2:
#             tmpsum = add
#             if l1:
#                 tmpsum += l1.val
#                 l1 = l1.next
#
#             if l2:
#                 tmpsum += l2.val
#                 l2 = l2.next
#
#             add = tmpsum // 10
#             tmpnode.next = ListNode(tmpsum % 10)
#             tmpnode = tmpnode.next
#         if add != 0:  # 处理最后的进位
#             tmpnode.next = ListNode(add)
#         return res.next

l1=[2,4,3]#21
l2=[5,6,4]#43
s = Solution()
print(s.addTwoNumbers(l1,l2))

