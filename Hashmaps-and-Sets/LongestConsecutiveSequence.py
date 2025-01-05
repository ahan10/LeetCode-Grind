# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) # remove the duplicates
        longest = 0

        for num in nums:
            if num - 1 not in s: # if the number that should appear sequentially before this is not in the set, that means there can be a potential sequence starting from here
                            # id num-1 exists in the set, then it means that the sequence does not start from the current element and we skip this
                next_num = num + 1 # next num to expect is the current + 1
                length = 1 # since the sequence starts form this element, it will have a length of 1

                while next_num in s: # while the next expected num is in the set
                    length += 1 # increase the length
                    next_num += 1 # increase the next num to look for
                longest = max(length, longest) # once the next num is not present in the set, compare the length to the longest one and keep the greater one

        return longest

    # Time O(n)
    # Space: O(n)