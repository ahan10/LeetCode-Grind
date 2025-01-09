# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns

        t = m * n # total number of elements
        l, r = 0, t - 1 # left pointer at the start and right pointer at the end

        while l <= r: # while the pointers do not cross over
            middle = (l + r) // 2 # get the middle index
            i_middle = middle // n # the row index is the middle integer division by the number of rows
            j_middle = middle % n # the column index is the middle mod the number of rows
            mid = matrix[i_middle][j_middle] # get the middle vale and perform normal binary search

            if mid == target: # if the num at middle index is the target, return true, and job is done
                return True
            elif mid > target: # if the nums at middle index is larger than the target, then the number potentially lies between left pointer and middle, so now update the right pointer to just before the middle index
                r = middle - 1
            else: # if the nums at middle index is smaller than the target, then the number potentially lies between middle pointer and right pointer, so now update the left pointer to just after the middle index
                l = middle + 1

        return False

# Time: O(log(n * m))
# Space: O(1)