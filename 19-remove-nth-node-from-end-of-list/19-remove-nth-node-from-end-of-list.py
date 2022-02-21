# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        k = 0
        node = head
        while node:
            node = node.next
            k += 1
        k -= n
        if k == 0:
            head = head.next
            return head
        node = head
        print(k)
        for i in range(k-1):
            node = node.next
        node.next = node.next.next
        return head