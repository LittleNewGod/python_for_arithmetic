# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 8:57
# @Author  : Xin
# @File    : day71-复制带随机指针的链表.py
# @Software: PyCharm


# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 要求返回这个链表的深拷贝。
# 示例：
# day71-题目图
#
# 输入：
# {"$id": "1", "next": {"$id": "2", "next": null, "random": {"$ref": "2"}, "val": 2}, "random": {"$ref": "2"}, "val": 1}
#
# 解释：
# 节点
# 1
# 的值是
# 1，它的下一个指针和随机指针都指向节点
# 2 。
# 节点
# 2
# 的值是
# 2，它的下一个指针指向
# null，随机指针指向它自己。
#
# 提示：
# 你必须返回给定头的拷贝作为对克隆列表的引用。


# Definition for a Node.

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        cur = head
        while cur:
            node = Node(cur.val,None,None)
            node.next = cur.next
            cur.next = node
            cur = node.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        res = head.next
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            cur = cur.next
            if cur:
                tmp.next = cur.next
        return res