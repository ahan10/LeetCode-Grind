# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - ord('A')] += 1  # character frequency in the window

            while (r - l + 1) - max(counts) > k:  # we have more characters to flip as compared to the majority character; window is invalid
                counts[ord(s[l]) - ord('A')] -= 1  # we shrink the window to make it valid and loose the left most character so we remove it from the window
                l += 1

            longest = max(longest, (r - l + 1))

        return longest
# Time: O(n)
# Space: O(1)