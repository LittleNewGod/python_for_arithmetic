# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 21:05
# @Author  : Xin
# @File    : day8-盛最多水的容器.py
# @Software: PyCharm

# 给定n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。在坐标内画n条垂直线，垂直线i的两个端点分别为(i, ai)和(i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且n的值至少为2。
#
# 图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。
#
# 示例:
#
# 输入: [1, 8, 6, 2, 5, 4, 8, 3, 7]
# 输出: 49

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #暴力法，循环两次，时间复杂度O(n**2)
        # j=0
        # ans=0
        # for i in range(len(height)-1):
        #     a=i
        #     while a<len(height)-1:
        #         a += 1
        #         if(a<len(height) and height[i]>height[a]):
        #             j=height[a]*(a-i)
        #         else:
        #             j=height[i]*(a-i)
        #         if(ans<j):
        #             ans=j
        #
        # return ans

        #双指针法,只需循环一次，时间复杂度为O(n)
        #初始化数据，结果初始为0，左指针初始为0，右指针初始为最大索引值
        ans,l,r=1,0,len(height)-1

        if len(height)==2 and min(height[0],height[1])==0:
            return 0
        #当左指针值小于右指针值时循环
        while l<r:
            #比较左右指针对应值的大小，取小的相乘，再比较每个相乘后结果取大的
            ans = max(ans,min(height[l],height[r])*(r-l))
            #当左指针对应的值小于右指针对应值，左指针向右移一位，反之右指针向左移一位
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans

#height= [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1,2,1]
s= Solution()
print(s.maxArea(height))
