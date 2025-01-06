# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:  # while the list is not empty and there is a next element
            if head.val == head.next.val:  # if the value of current node and next node is same
                head.next = head.next.next  # point the current node to the note after the next
            else:
                head = head.next  # else move ahead

        return res

        # Time: O(n)
        # Space: O(1) {since we modify the existing list}
