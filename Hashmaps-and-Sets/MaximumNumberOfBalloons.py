# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/description/

from collections import defaultdict # default dict is a dict that if an element is not in the in it adds and makes it value 0

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = 'balloon'

        for c in text:  # O(n)
            if c in balloon: # counts the number of b, a, l, o nad n's
                counter[c] += 1

        if any(c not in counter for c in balloon):  # O(1) # if any of the b, a, l, o, n is not in the counter, then we can't make balloon so we return 0
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n']) # return the min value of characters

        # Time: O(n)
        # Space: O(1)