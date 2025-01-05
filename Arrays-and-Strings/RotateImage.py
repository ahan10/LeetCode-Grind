# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # step 1: transpose, swap i, j's
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # step 2: flip from middle (vertically)
        for i in range(n):
            for j in range(n // 2): # since we only need to switch i to j and not the inverse
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
                # we fixed an i, that is we are stuck at a row
                # assume j as the left pointer going right
                # n - j - 1 right pointer going left
                # basically we are squeezing inwards and swapping those

# Time: (n^2)
# Space: O(1)




