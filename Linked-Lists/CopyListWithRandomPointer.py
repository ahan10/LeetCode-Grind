# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None # if empty LL, return null

        curr = head # point current to head
        old_to_new = {} # hashmap where keys are old nodes and vales are deep copy of nodes

        while curr: # traverse the whole LL, this time only making deep copy of the nodes
            node = Node(x=curr.val) # deep copy the current node, without the next and random, by default they are set null
            old_to_new[curr] = node # put the current node (from original list) as the key and deep copy as the head
            curr = curr.next # move over

        curr = head # reset the curr
        while curr: # traverse the whole LL, this time assigning the next and random to the new LL from head
            new_node = old_to_new[curr] # get the deep copied node to set its next and random
            new_node.next = old_to_new[curr.next] if curr.next else None # set the deep copy's next by getting the new deep copy next node from hashmap
            new_node.random = old_to_new[curr.random] if curr.random else None # set the deep copy's random by getting the new deep copy random node from hashmap
            curr = curr.next # move over

        return old_to_new[head] # return the head node's value from the hashmap, which in turn will return the deep copied LL

# Time: O(n)
# Space: O(n)