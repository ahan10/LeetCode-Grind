# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_length = float('inf')

        for s in strs: # we need ot find the minimum length of the string so that we do not run out of the index out of bounds error
            min_length = min(min_length, len(s))

        i = 0
        while i < min_length: #we iterate over the first min_length characters
            for s in strs:
                if s[i] != strs[0][i]: #if the current character doesn't match the character at this index in the first string, then we return the first i charachters
                    return s[:i]
            i += 1

        return strs[0][:i] #if we ran till min_length or the length is 0, we run till then
    # Time: O(n * m) where n is the number of strings, m is the min word length
    # Space: O(1)