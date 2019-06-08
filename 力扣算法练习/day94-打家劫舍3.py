# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 20:32
# @Author  : Xin
# @File    : day94-打家劫舍3.py
# @Software: PyCharm


# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#解法一：
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        def helper(root):
            if root==None:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)
            rob = root.val + left[1] + right[1]
            skip = max(left) + max(right)
            return [rob, skip]
        res = helper(root)
        return max(res)



#解法二：
"""
解题思路：
题目要求是判断从根节点到叶子节点相加的值是否为为sum，
应该想到使用递归，
第一种方法是用递归逐个减去节点值然后判断叶子节点和sum是否相等，
第二种方法是借助变量，逐个累加节点到叶子节点，然后判断
代码采取第一种方式
"""
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(0, root)]
        result = {None: (0, 0)}
        while stack:
            rob, node = stack.pop()
            if not node:
                continue

            if not rob:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                result[node] = (result[node.left][1] + result[node.right][1] + node.val, \
                                max(result[node.left]) + max(result[node.right]))
        return max(result[root])