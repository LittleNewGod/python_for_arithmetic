# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 20:49
# @Author  : Xin
# @File    : day65-验证二叉搜索树.py
# @Software: PyCharm

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res, _, _ = self.isValidBST2(root)
        return res

    def isValidBST2(self, root):
        if not root:
            return True, None, None
        valid_left, min_left, max_left = self.isValidBST2(root.left)
        valid_right, min_right, max_right = self.isValidBST2(root.right)
        if not valid_left or not valid_right:
            return False, None, None
        if valid_left and valid_right and ((max_left and root.val > max_left) or not max_left) and (
                (min_right and root.val < min_right) or not min_right):
            return True, min_left if min_left else root.val, max_right if max_right else root.val
        return False, None, None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.l = []
        self.for_each(root)
        return sorted(list(set(self.l))) == self.l # 验证是否有重复元素，并且是否是有序的

    def for_each(self, root):
        if not root:
            return
        # 中序遍历
        self.for_each(root.left)
        self.l.append(root.val)
        self.for_each(root.right)
