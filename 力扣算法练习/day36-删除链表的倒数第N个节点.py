# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 8:54
# @Author  : Xin
# @File    : day36-删除链表的倒数第N个节点.py
# @Software: PyCharm

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        p, q = h, h

        for _ in range(n + 1):
            q = q.next

        while q != None:
            p = p.next
            q = q.next

        p.next = p.next.next
        return h.next