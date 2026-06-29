"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        hashMap = {}

        def dfs(node: Optional['Node']):
            if node in hashMap:
                return hashMap[node]

            cloneNode = Node(node.val)
            hashMap[node] = cloneNode
            
            tmpList = []
            for n in node.neighbors:
                tmpList.append(dfs(n))
            cloneNode.neighbors = tmpList

            return cloneNode
            
        return dfs(node)