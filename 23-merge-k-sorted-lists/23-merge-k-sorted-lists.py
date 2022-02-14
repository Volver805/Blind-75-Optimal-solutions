# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        res = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(res, node.val)
                node = node.next
        head = node = ListNode()
        if not res:
            return None
        while len(res) > 1:
            node.val = heapq.heappop(res)
            node.next = ListNode()
            node = node.next
        node.val = heapq.heappop(res)
        return head