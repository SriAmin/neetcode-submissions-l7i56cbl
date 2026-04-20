# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        if head == None or head.next == None or head.next.next == None:
            return False
        f = head.next.next
        print(s.val)
        print(f.val)

        while f != None:
            if s == f:
                return True
            s = s.next

            if f.next == None:
                return False

            f = f.next.next

        return False