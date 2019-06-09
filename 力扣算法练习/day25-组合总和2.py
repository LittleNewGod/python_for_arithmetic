# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 10:54
# @Author  : Xin
# @File    : day25-组合总和2.py
# @Software: PyCharm

# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.combin(result,[],candidates,target)
        return result

    def combin(self,result,num,candidates,target):
        if target == 0:
            result.append(list(num))
            return
        for i in range(len(candidates)):
            if candidates[i]>target or candidates[i] in candidates[:i]:
                continue
            num.append(candidates[i])
            self.combin(result,num,candidates[i+1:],target-candidates[i])
            num.pop()

        return


candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
print(s.combinationSum(candidates,target))
