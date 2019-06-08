# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 20:30
# @Author  : Xin
# @File    : day96-平衡二叉树.py
# @Software: PyCharm

# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。

# 是平衡二叉树的条件：
# 左子树是平衡二叉树。
# 右子树是平衡二叉树。
# 左右子树之间的深度不超过1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        depth_left, depth_right = self.depth(root.left), self.depth(root.right)
        if abs(depth_left - depth_right) < 2:
            return True
        else:
            return False

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
