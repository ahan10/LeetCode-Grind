# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs: # n
            count = [0] * 26 # since there are 26 alphabets, and each value at the index corresponds to the frequency of that alphabet
            for c in s:
                count[ord(c) - ord("a")] += 1 # count frequency of that element by subtracting the ASCII of that character from that of a to bet it in the range of 0-26
            key = tuple(count) # since tuples are not mutable, they can be the keys for the hashmap
            anagrams_dict[key].append(s) # add the string to the key

        return list(anagrams_dict.values()) # convert the values ot a list and return it, they are already grouped

# Time: O(n * m)
# Space: O(n * m)