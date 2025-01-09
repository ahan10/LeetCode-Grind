# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n # set the pointer at the first and last index

        while l < r: # while they don't overlap
            m = (l + r) // 2 # get the middle index

            if isBadVersion(m): # if the middle version is a bad version, we are guaranteed that versions to right of it are bad, so we move right to middle
                r = m
            else: # else, we know that versions till m are good, so it must lie in the range of middle+1 to right
                l = m + 1
        return l # when we exit the loop, l = r, so return either l or r