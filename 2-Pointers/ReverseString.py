# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # pointers to the left and right
        left = 0
        right = len(s) - 1

        while left < right: # continue till the pointers do not overlap
            s[left], s[right] = s[right], s[left] # swap the two elements
            # move the pointers
            left += 1
            right -= 1

# Time: O(n)
# Space: O(1)