# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers left and right
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum(): # if the current left element is not an alphabet or number move right
                l += 1
                continue

            if not s[r].isalnum(): # if the current right element is not an alphabet or number move left
                r -= 1
                continue

            if s[l].lower() != s[r].lower(): # if the current left and right elements are both either alphabet or number but not equal, return false
                return False

            # move the indexes
            l += 1
            r -= 1

        return True

# Time: O(n)
# Space: O(1)