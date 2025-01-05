# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/description/
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_map = Counter(magazine) # TC for Counter is O(n)

        for c in ransomNote:
            if c not in freq_map: # if the element for ransom note is not in magazine, it can't be reconstructed
                return False
            elif freq_map[c] == 1: # if value of the character in magazine map is 1, then we delete it
                del freq_map[c]
            else:
                freq_map[c] -= 1

        return True
# Time: O(R + M)  -> R = len(ransomNote), M = len(magazine)
# Space: O(M)     -> we're using a hashmap