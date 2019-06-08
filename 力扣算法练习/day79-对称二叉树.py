# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 22:33
# @Author  : Xin
# @File    : day79-对称二叉树.py
# @Software: PyCharm

# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#解法一：递归
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left,node2.right) and check(node1.right, node2.left)
        return check(root,root)

#解法二：迭代：其实就是层序遍历，然后检查每一层是不是回文数组
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        queue = [root]

        while (queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)

            if layer != layer[::-1]:
                return False
            queue = next_queue

        return True