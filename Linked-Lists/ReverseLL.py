# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # current node points to the first node/ head
        prev = None # points to the previous node of current. Initially there is nothing to the left of head

        while curr: # until we reach the end of list
            temp = curr.next # store the current node in a temp variable
            curr.next = prev # the next node for the current one become the previous node, essentially reversing it
            prev = curr # move the prev pointer ahead
            curr = temp # move the curr pointer ahead

        return prev # at the end previous will have stored the reverse list
    # Time: O(n)
    # Space: O(n)