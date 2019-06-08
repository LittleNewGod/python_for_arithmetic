# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 22:21
# @Author  : Xin
# @File    : day69-克隆图.py
# @Software: PyCharm

# 给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值
# val（Int） 和其邻居的列表（list[Node]）。
#
# 示例：
# day69题目图
# 输入：
# {"$id": "1", "neighbors": [{"$id": "2", "neighbors": [{"$ref": "1"}, {"$id": "3", "neighbors": [{"$ref": "2"},
#                                                                                                 {"$id": "4",
#                                                                                                  "neighbors": [
#                                                                                                      {"$ref": "3"},
#                                                                                                      {"$ref": "1"}],
#                                                                                                  "val": 4}], "val": 3}],
#                             "val": 2}, {"$ref": "4"}], "val": 1}
#
# 解释：
# 节点1的值是1，它有两个邻居：节点2和4 。
# 节点2的值是2，它有两个邻居：节点1和3 。
# 节点3的值是3，它有两个邻居：节点2和4 。
# 节点4的值是4，它有两个邻居：节点1和3 。
#
# 提示：
#
# 节点数介于1到100之间。
# 无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
# 由于图是无向的，如果节点p是节点q的邻居，那么节点q也必须是节点p的邻居。
# 必须将给定节点的拷贝作为对克隆图的引用返回。


# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        m = {}
        queue = [node]
        m[node] = Node(node.val, [])
        while queue:
            current_node = queue.pop(0)
            for nodes in current_node.neighbors:
                if nodes not in m:
                    m[nodes] = Node(nodes.val, [])
                    queue.append(nodes)
                m[current_node].neighbors.append(m[nodes])
        return m[node]

node = {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
s = Solution()
print(s.cloneGraph(node))