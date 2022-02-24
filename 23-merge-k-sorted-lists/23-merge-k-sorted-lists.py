# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        i = 1
        k = len(lists)
        if not lists:
            return
        while i < k:
            for j in range(0, k-i, i*2):
                lists[j] = self.merge(lists[j], lists[j+i])
            i *= 2
        return lists[0]
                
    def merge(self, list1, list2):
        # From 21.Merge Two Sorted Lists Problem
        head = prev = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                prev.next = temp
                prev = temp
            else:
                temp = list2
                list2 = list2.next
                prev.next = temp
                prev = temp
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        return head.next