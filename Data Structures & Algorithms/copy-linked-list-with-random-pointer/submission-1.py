"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = {}
        curr = head
        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        
        for real, copy in nodes.items():
            if real.next:
                copy.next = nodes[real.next]
            if real.random:
                copy.random = nodes[real.random]

        return nodes[head]
        