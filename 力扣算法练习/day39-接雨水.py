# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:23
# @Author  : Xin
# @File    : day39-接雨水.py
# @Software: PyCharm


# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# day39图
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

#解法：
# 1.找出最高点
# 2.分别从两边往最高点遍历：如果下一个数比当前数小，说明可以接到水
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=1: return 0
        max_height=0
        max_height_index = 0
        #找到最高点
        # for i in range(len(height)):
        #     h = height[i]
        #     if h > max_height:
        #         max_height=h
        #         max_height_index=i

        max_height=max(height)
        max_height_index=height.index(max_height)

        #初始化面积参数
        area = 0

        #从左边往最高点遍历
        tmp = height[0]
        for i in range(max_height_index):
            if height[i]>tmp:
                tmp=height[i]
            else:
                area=area+(tmp-height[i])

        #从右边往最高点遍历
        tmp = height[-1]
        # for i in reversed(range(max_height_index+1,len(height))):
        #     if height[i]>tmp:
        #         tmp=height[i]
        #     else:
        #         area=area+(tmp-height[i])
        for i in range(len(height)-1,max_height_index,-1):
            if height[i]>tmp:
                tmp=height[i]
            else:
                area=area+(tmp-height[i])

        return area

height= [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(height))

