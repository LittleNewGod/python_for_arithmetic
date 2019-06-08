# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 9:40
# @Author  : Xin
# @File    : day78-文本左右对齐.py
# @Software: PyCharm

# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
# 示例:
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# 示例 2:
#
# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。
#      第二行同样为左对齐，这是因为这行只包含一个单词。
# 示例 3:
#
# 输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

#解法一：
# class Solution(object):
#     def fullJustify(self, words, maxWidth):
#         """
#         :type words: List[str]
#         :type maxWidth: int
#         :rtype: List[str]
#         """
#         res = []
#         i = 0
#         n = len(words)
#         while i < n:
#             left = i
#             all_num = len(words[i])
#             i += 1
#             while i < n and all_num + 1 + len(words[i]) <= maxWidth:
#                 all_num += (1 + len(words[i]))
#                 i += 1
#             tmp = words[left:i]
#             if i == n:
#                 tmp_str = " ".join(tmp)
#                 tmp_str += " " * (maxWidth - len(tmp_str))
#                 res.append(tmp_str)
#                 break
#             remain_space = maxWidth - sum(map(len, tmp))
#             if i - left - 1 == 0:
#                 a = 0
#                 b = 0
#             else:
#                 a, b = divmod(remain_space, i - left - 1)
#             j = 0
#             tmp_str = ""
#             while b:
#                 tmp_str += tmp[j] + " " * (a + 1)
#                 j += 1
#                 b -= 1
#             while j < len(tmp):
#                 tmp_str += tmp[j] + " " * a
#                 j += 1
#             if len(tmp_str) < maxWidth:
#                 tmp_str += " " * (maxWidth - len(tmp_str))
#             else:
#                 tmp_str = tmp_str[:maxWidth]
#             res.append(tmp_str)
#         return res


#解法二：
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return ['']
        result = []
        i = 0
        tmpLen = 0  # 记录当前行单词+' '的长度
        counts = 0  # 记录当前行的单词个数
        while i < len(words):
            if tmpLen + len(words[i]) <= maxWidth:
                tmpLen += len(words[i]) + 1
                i += 1
                counts += 1
            else:
                numSpace = maxWidth - tmpLen + counts  # 空格总数
                # print(i,numSpace,(tmpLen,counts))
                if counts == 1:
                    result.append(words[i-1]+' '*numSpace)
                else:
                    eachNum = numSpace // (counts-1)  # 单词之间应放的空格数
                    restNum = numSpace % (counts-1)  # 剩余空格数
                    tmp = ''
                    start = i - counts
                    while start < i - 1:
                        if restNum > 0:
                            print(' ' * (eachNum + 1),eachNum + 1)
                            tmp = tmp + words[start] + ' ' * (eachNum + 1)
                            restNum -= 1
                            start += 1
                        else:
                            tmp = tmp + words[start] + ' ' * eachNum
                            start += 1
                    tmp = tmp + words[i-1]
                    result.append(tmp)
                tmpLen = 0
                counts = 0
        # 最后一行
        if counts != 0:
            j = counts
            tmp = ''
            while j > 1:
                tmp = tmp + words[i-j] + ' '
                j -= 1
            tmp = tmp + words[i-1]
            tmp = tmp + ' ' * (maxWidth-len(tmp))
            result.append(tmp)
        return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
s = Solution()
print(s.fullJustify(words,maxWidth))