# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None or head.next.next == None:
            return False
        s = head
        f = head.next.next

        while f != None:
            if s == f:
                return True
                
            if f.next == None:
                return False

            s = s.next
            f = f.next.next

        return False