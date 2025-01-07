# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Time: O(n)
# Space: O(1)
# for both

# slow and fast pointer approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head #  initially both slow and fast point at the same place

        while fast and fast.next: # while fast is not null i.e. we have not reached end and there is an element after fast, i.e. not the last element
            slow = slow.next # slow moves at 1x
            fast = fast.next.next # slow moves at 2x

        return slow
    # since fast moves at 2x as compared to slow, so we are guaranteed that when fast reaches at the end, slow will be at the middle, so we return slow

# trivial solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr1 = head
        length = 0

        while curr and curr.next: # loop to count the length of the LL
            length += 1
            curr = curr.next

        middle = length // 2 # find the middle index

        while middle > 0: #we decrement middle till it reaches 0, and return the list we have then
            middle -= 1
            curr1 = curr1.next
        return curr1

