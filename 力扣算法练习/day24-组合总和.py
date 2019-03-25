# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 21:50
# @Author  : Xin
# @File    : day24-组合总和.py
# @Software: PyCharm

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

#解法一：递归
# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#
#         def dfs(results, result, candidates, target, level):
#             if target == 0:
#                 results.append(list(result))
#                 return
#             elif target > 0:
#                 for i in range(level, len(candidates)):
#                     result.append(candidates[i])
#                     dfs(results, result, candidates, target - candidates[i], i)
#                     result.pop()
#
#         results = []
#         dfs(results, [], candidates, target, 0)
#         return results
#
# candidates = [2,3,6,7]
# target = 7
# s = Solution()
# print(s.combinationSum(candidates,target))

#解法二：在解法一的基础上进行优化，减少循环次数，以及封装一下
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.combin(result,[],candidates,target,0)
        return result

    def combin(self,result,num,candidates,target,flag):
        if target == 0:
            result.append(list(num))
            return
        elif target > 0:
            for i in range(flag,len(candidates)):
                num.append(candidates[i])
                self.combin(result,num,candidates,target-candidates[i],i)
                num.pop()
                continue


candidates = [2,3,6,7]
target = 7
s = Solution()
print(s.combinationSum(candidates,target))
