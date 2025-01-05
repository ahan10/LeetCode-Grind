# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # can't be an anagram is the lengths are not same
            return False

        # make hashmap/ dict
        s_map = Counter(s)
        t_map = Counter(t)

        return s_map == t_map # anagram is the dict is same

# Time: O(n)
# Space: O(n)