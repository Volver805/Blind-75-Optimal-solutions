# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        parent = head
        curr = head.next
        head.next = None
        while curr:
            next = curr.next
            curr.next = parent
            parent = curr
            curr = next
        return parent