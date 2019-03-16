# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 20:54
# @Author  : Xin
# @File    : day17-合并K个排序链表.py
# @Software: PyCharm


# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 示例:
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        else:
            ls = []
            for i in lists:
                while(i!=None):
                    ls.append(i.val)
                    i = i.next
            ls.sort()
            try:
                start = ListNode(ls[0])
            except:
                return None
            else:
                try:
                    s2 = ListNode(ls[1])
                except:
                    return start
                else:
                    start.next = s2
                    for i in range(2,len(ls)):
                        s2.next = ListNode(ls[i])
                        s2 = s2.next


lists= ListNode([[1,4,5],[1,3,4],[2,6]])
s=Solution()
print(s.mergeKLists(lists))