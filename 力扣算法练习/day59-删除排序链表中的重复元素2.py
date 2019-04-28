# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 10:19
# @Author  : Xin
# @File    : day59-删除排序链表中的重复元素2.py
# @Software: PyCharm


# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)  # 创建新链表头
        p.next = head
        head = p  # 新的链表头

        while p.next:
            left = p.next  # 左指针,p为当前节点的上一个节点
            right = left  # 右指针
            # 若值相同，则移动右指针，直到右指针下一个节点的值不同为止
            while right.next and (right.next.val == left.val):
                right = right.next
            if right == left:  # 左右指针相同，则表示不重复
                p = p.next
            else:  # 左右指针不同，则删除左节点到右节点之间的所有节点
                p.next = right.next

        # 返回新链表头
        return head.next

head = [1,2,3,3,4,4,5]
