# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode() # make a dummy head
        curr = dummy # point our current to dummy

        while list1 and list2: #while both the lists are in bounds
            if list1.val < list2.val: # if the value of list1 node is less than that of list2, we need list1's node
                curr.next = list1 # point the current to list1 node
                curr = list1 # make the current the list1 head node
                list1 = list1.next # iterate over to the next element
            else: # else either list2 node is less than that of list1 or equal, then
                curr.next = list2 # point the current to list2 node
                curr = list2 # make the current the list2 head node
                list2 = list2.next # iterate over to the next element

        if list1: # if we have nodes left in our list1 after the loop, meaning that list2 is over
            curr.next = list1 # just append the rest of the list1
        else: # else either the list1 was empty or both are empty
            curr.next = list2 # just append the rest of the list2

        return dummy.next #since the dummy head is 0, we return the list after it

    # Time: O(n) (n = length of the longer list)
    # Space: O(1)


