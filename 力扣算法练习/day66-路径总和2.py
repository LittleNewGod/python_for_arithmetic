# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 20:34
# @Author  : Xin
# @File    : day66-路径总和2.py
# @Software: PyCharm

# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 注意temp与temp[:]的区别，后者是第一层深拷贝，会生成两个不同的list
class Solution(object):
    def pathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        def dfs(root, Sum, ans, temp):
            if root == None:
                return
            temp.append(root.val)
            if root.left == None and root.right == None and Sum - root.val == 0:
                ans.append(temp[:])  # 找到一条OK的路了

            dfs(root.left, Sum - root.val, ans, temp)
            dfs(root.right, Sum - root.val, ans, temp)
            temp.pop()

        ans = []
        temp = []
        dfs(root, Sum, ans, temp)
        return ans
