# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n != 0:
            return None
        output = head
        front, back = head, head
        for _ in range(n-1):
            front = front.next
        print(front.val)
        print(back.val)
        prev_node = back
        if front.next == None:
            return back.next
        while front:
            if front.next == None:
                prev_node.next = back.next
            else:
                prev_node = back
                back = back.next
            front = front.next
        return output