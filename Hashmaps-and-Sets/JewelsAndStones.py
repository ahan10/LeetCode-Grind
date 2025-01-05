# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels) # we make a set of the jewels
        count = 0
        for stone in stones:
            if stone in s: # if the stone is in jewels then we increase the counter and at the end return
                count += 1
        return count

# Time: O(n + m)
# Space: O(n)