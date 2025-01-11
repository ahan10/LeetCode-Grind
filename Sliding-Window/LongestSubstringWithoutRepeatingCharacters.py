# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# variable sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 # left pointer
        sett = set() # set of letters in our window
        longest = 0 # longest substring that we have encountered
        n = len(s) # length of the string

        for r in range(n): # we want to traverse through the whole array until we reach the end by the right pointer
            while s[r] in sett: # invalid window, since there is a repeating character
                sett.remove(s[l]) # if there is a repeating character, we remove the first letter of the window assuming it is the duplicate one
                l += 1 # and move the window ahead

            # we keep on removing the left character until the set becomes valid if we add the right character, to maintain a valid window

            w = (r - l) + 1 # length of the window
            longest = max(longest, w) # get the max

            sett.add(s[r]) # when we reach here, we are guaranteed that the right character does not exist in the set so we can easily add it

        return longest

    # Time: O(n); even though there are two loops, only the for loop runs for n times, and while loop doesn't run for the whole n iterations