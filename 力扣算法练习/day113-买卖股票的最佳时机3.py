# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         day113-买卖股票的最佳时机3
# Author:       xin
# Date:         2019/6/30
# IDE:  PyCharm
# -------------------------------------------------------------------------------

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
# 示例 3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。


#解法一：标准的三维DP动态规划，三个维度，第一维表示天，第二维表示交易了几次，
# 第三维表示是否持有股票。与下面188题买卖股票4一样的代码，把交易k次定义为2次。当然也可以把内层的for循环拆出来，
# 分别列出交易0次、1次、2次的状态转移方程即可

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices:
#             return 0
#         n = len(prices)
#         dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
#         # dp[i][j][0]表示第i天交易了j次时不持有股票, dp[i][j][1]表示第i天交易了j次时持有股票
#         # 定义卖出股票时交易次数加1
#         for i in range(3):
#             dp[0][i][0], dp[0][i][1] = 0, -prices[0]
#
#         for i in range(1, n):
#             for j in range(3):
#                 if not j:
#                     dp[i][j][0] = dp[i - 1][j][0]
#                 else:
#                     dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
#                 dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
#
#         return max(dp[n - 1][0][0], dp[n - 1][1][0], dp[n - 1][2][0])
#
# prices = [3,3,5,0,0,3,1,4]
# s = Solution()
# print(s.maxProfit(prices))


#解法二：用变量而不是多维数组保存迭代的值，优点是省内存空间，缺点是不是标准DP，没法泛化

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0
        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])  # 用负值统一变量
            sell1 = max(sell1, buy1 + prices[i])  # sell1为 0~i(含)天股市中买卖一次的最优利润
            buy2 = max(buy2, sell1 - prices[i])  # 仅当＞0才会更新，保证 第二次买入不会与第一次卖出为同一天。而sell1为历史记录保证第二次买入比第一次卖出晚。
            sell2 = max(sell2, buy2 + prices[i])  # 若第二轮买卖为同一天，则不会更新。此操作自然保证sell2为买卖至多两次的最优利润。
        return sell2

prices = [3,3,5,0,0,3,1,4]
s = Solution()
print(s.maxProfit(prices))
