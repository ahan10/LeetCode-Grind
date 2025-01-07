# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode() # dummy node
        dummy.next = head # attach the dummy node in front of the LL
        A = B = dummy # make 2 pointers A = ahead; B = behind; and they point to the dummy node

        for _ in range(n + 1): # put the ahead pointer at n + 1 position
            A = A.next

        while A: # while the ahead pointer does not go out of bounds, keep moving both ahead and behind by 1 in right direction
            B = B.next
            A = A.next
            # once the ahead pointer reaches out of bounds, the behind pointer points just before the node to be removed, so skip it
        B.next = B.next.next

        return dummy.next # return the LL from dummy.next, and not head since there can be a case, where the head is removed and we just return null

# Time: O(M); M is the length of the LL
# Space: O(1)