# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Fast and SLow Pointer Approach

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode() # make a dummy node
        dummy.next = head # attach the dummy node in front of the Linked List
        slow = fast = dummy # make 2 pointers fast and slow, fast moves at 2x speed as compared to slow

        while fast and fast.next: # while the fast has not reached null i.e end of the LL or is not the last node in the LL
            fast = fast.next.next # move at 2x speed
            slow = slow.next # move at 1x speed

            if slow == fast: # if at any time the nodes become equal; there is a cycle
                return True

        # if we quit the loop that means there is no cycle, and we return false
        return False

    # Time: O(n)
    # Space: O(1)

    # Hashing Approach
    class Solution:
        def hasCycle(self, head: Optional[ListNode]) -> bool:
            hash_set = set() # initialize an empty se

            dummy = head # assign dummy to the head

            while dummy: # while we have not reached the end
                if dummy in hash_set: # if the node (not the value) is already in set, we have a cycle
                    return True
                else:                 # else just add that to the set and move ahead
                    hash_set.add(dummy)
                dummy = dummy.next
            return False              # return false outside the loop, meaning that the there is no cycle to be found