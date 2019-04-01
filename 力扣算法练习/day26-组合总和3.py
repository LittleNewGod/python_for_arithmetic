# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 22:10
# @Author  : Xin
# @File    : day26-组合总和3.py
# @Software: PyCharm

# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = [x for x in range(1, 10)]

        def dfs(path, istart, target, cnt):
            # print istart, candidates[istart], path, target, cnt
            if target == 0 and cnt == k:
                res.append(path)
                return
            elif istart < len(candidates) and candidates[istart] > target or cnt > k:
                return
            else:
                index = istart
                while index < len(candidates):
                    if candidates[index] > target:
                        break
                    else:
                        dfs(path + [candidates[index]], index + 1, target - candidates[index], cnt + 1)
                    while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                        index += 1
                    if index == len(candidates) - 1:
                        break
                    index += 1

        dfs([], 0, n, 0)
        return res

s = Solution()
ans = s.combinationSum3(3,7)
print(ans)