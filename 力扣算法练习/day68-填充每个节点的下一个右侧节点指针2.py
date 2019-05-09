# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 10:38
# @Author  : Xin
# @File    : day68-填充每个节点的下一个右侧节点指针2.py
# @Software: PyCharm

# 给定一个二叉树
#
# struct
# Node
# {
#     int
# val;
# Node * left;
# Node * right;
# Node * next;
# }
# 填充它的每个
# next
# 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将
# next
# 指针设置为
# NULL。
#
# 初始状态下，所有
# next
# 指针都被设置为
# NULL。
#
# 示例：
# day68-题目图
#
# 输入：{"$id": "1",
#     "left": {"$id": "2", "left": {"$id": "3", "left": null, "next": null, "right": null, "val": 4}, "next": null,
#              "right": {"$id": "4", "left": null, "next": null, "right": null, "val": 5}, "val": 2}, "next": null,
#     "right": {"$id": "5", "left": null, "next": null,
#               "right": {"$id": "6", "left": null, "next": null, "right": null, "val": 7}, "val": 3}, "val": 1}
#
# 输出：{"$id": "1", "left": {"$id": "2", "left": {"$id": "3", "left": null, "next": {"$id": "4", "left": null,
#                                                                                  "next": {"$id": "5", "left": null,
#                                                                                           "next": null, "right": null,
#                                                                                           "val": 7}, "right": null,
#                                                                                  "val": 5}, "right": null, "val": 4},
#                          "next": {"$id": "6", "left": null, "next": null, "right": {"$ref": "5"}, "val": 3},
#                          "right": {"$ref": "4"}, "val": 2}, "next": null, "right": {"$ref": "6"}, "val": 1}
#
# 解释：给定二叉树如图
# A
# 所示，你的函数应该填充它的每个
# next
# 指针，以指向其下一个右侧节点，如图
# B
# 所示。
#
#
# 提示：
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

#解析：使用collections的deque,连同层数一起入队列，设置变量记录前一个的层数和节点，设置变量记录当前的层数和节点，根据前一个节点的层数和当前层数是否相等进行不同的操作 ，相同在本层，不同则进入下一层
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        from collections import deque
        if root == None:
            return None
        queue = deque()
        queue.append((0,root))
        predepth = -1
        curdepth = -1
        pre = None
        cur = None
        while queue:
            curdepth,cur = queue.popleft()
            if cur.left != None:
                queue.append((curdepth+1, cur.left))
            if cur.right != None:
                queue.append((curdepth+1,cur.right))
            if predepth != curdepth:
                cur.next = None
                pre = cur
                predepth = curdepth
            else:
                pre.next = cur
                pre = pre.next
        return root


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#解法二：
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        a = [root, None]
        while any(a):
            for i in range(len(a)):
                if a[i] is not None:
                    a[i].next = a[i + 1]
            b = []
            for x in a:
                if x != None:
                    if x.left is not None:
                        b.append(x.left)
                    if x.right is not None:
                        b.append(x.right)
            a = b
            a.append(None)

        return root