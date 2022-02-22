# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        node = head
        while prev.next:
            temp = prev
            prev = prev.next
            temp.next = node.next
            node.next = temp
            node = node.next.next
        return head