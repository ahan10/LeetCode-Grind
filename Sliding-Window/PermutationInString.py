# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        l = 0

        count1 = [0] * 26 # count of characters of s1
        count2 = [0] * 26 # count of characters of s2

        for s in s1: # make the s1 counter
            count1[ord(s) - ord('a')] += 1

        for r in range(n): # make the sliding window
            count2[ord(s2[r]) - ord('a')] += 1 # we are making counter for the sliding window

            if (r - l + 1) == k: # since all the permutations of size of s1 will be of length n1/ k, window will be only valid when the window is of size n1/ k
                if count1 == count2: # if the counts of both s1 and the window of s2 is equal, we have found hte permutation
                    return True
                count2[ord(s2[l]) - ord('a')] -= 1 # else, we need to slide the window, we will lose the left most character as we slide over
                l += 1

        return False # after the loop, we return false since we didn't find a valid permutation of s1 in s2

# Time: O(n2) {n2 = length of s2}
# Space: O(1)