# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} # make a dictionary and store all the numeric values corresponding to the the roman values
        summ = 0 # initially the sum is 0
        n = len(s)
        i = 0 # i is at the first index
        while i < n: # while we do not traverse the whole string
            if i < n - 1 and d[s[i]] < d[s[i + 1]]: # if there is an element after the current element, and the current element is smaller than the one after it
                summ += d[s[i + 1]] - d[s[i]] # then we subtract the smaller from bigger
                i += 2  # and since we used 2 indexes, we move ahead 2
            else:
                summ += d[s[i]] # else we just add the current value and move ahead
                i += 1

        return summ

    # Time: O(n)
    # Space: O(1)