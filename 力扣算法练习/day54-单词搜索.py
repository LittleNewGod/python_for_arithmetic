# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 12:17
# @Author  : Xin
# @File    : day54-单词搜索.py
# @Software: PyCharm

#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        max_x, max_y, max_step = len(board)-1, len(board[0])-1, len(word)-1
        def maze(x, y,step,visited):
            if visited[x][y]==1:
                return False
            if board[x][y] != word[step]:
                return False
            if step==max_step:
                return True
            visited[x][y]=1
            if x < max_x and maze(x+1,y,step+1,visited):
                return True
            if x>0 and maze(x-1,y,step+1,visited):
                return True
            if y<max_y and maze(x,y+1,step+1,visited):
                return True
            if y>0 and maze(x,y-1,step+1,visited):
                return True
            # 记得失败后要置零
            visited[x][y]=0
            return False
        visited=[[0]*(max_y+1) for _ in range(max_x+1)]
        for x in range(max_x+1):
            for y in range(max_y+1):
                if board[x][y] != word[0]:
                    continue
                if maze(x,y,0,visited):
                    return True
        return False


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word='ABCCED'
s=Solution()
print(s.exist(board,word))