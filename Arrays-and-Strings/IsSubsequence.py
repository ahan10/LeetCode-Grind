# 392. Is Subsequence (Find if s is substring of T)
# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if S > T: # if the S is bigger than T, subsequence cannot exist
            return False
        if s == '': # if the checking string (s) is empty, it is automatically true
            return True

        j = 0 # j is the index for the string s that we need to find if it exists in t
        for i in range(0, T): # iterate the bigger string
            if t[i] == s[j]: # if the characters match
                if j == S - 1: # if we have traversed the whole of string s, that means we found the subsequence and return true
                    return True
                j += 1 # if we found only one of the characters then move to the other characters

        return False # if we had a subsequence, we would have found it in the loop, so we just return False
 # Time: O(T)
 # Space: O(1)