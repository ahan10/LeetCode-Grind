# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: # base case: if number of rows is 1 we can skip all of this
            return s

        i = 0 # the row in which we want to append
        d = 1 # the direction we want to move, 1 is down and -1 is up

        rows = [[] for _ in range(numRows)] # we make a 2D array with number of rows as desired

        for char in s: # iterate over the string
            rows[i].append(char) # append the character at the desired row

            if i == 0: # if i == 0, we need to move down so we set the direction as 1
                d = 1
            elif i == numRows - 1: # if i == numRows - 1; we have reached the end, and we need to start moving u, that is direction -1
                d = -1

            i += d # this is done since when we are moving down d is 1, so i in incremented, and when we are moving up, d is -1, so i is decremented

        ret = '' # return string

        for i in range(numRows): # iterate over all the number of rows in matrix
            ret += ''.join(rows[i]) # append each row

        return ret

    # Time: O(n * R) {R = number of rows}
    # Space: O(numRows + n)