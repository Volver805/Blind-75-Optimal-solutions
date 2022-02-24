# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        if not heap:
            return 
        head = node = ListNode(heapq.heappop(heap))
        while heap:
            node.next = ListNode()
            node = node.next
            node.val = heapq.heappop(heap)
        node = None
        return head