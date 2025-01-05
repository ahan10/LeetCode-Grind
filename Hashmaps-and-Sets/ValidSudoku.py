# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate Rows
        for i in range(9):
            s = set() # make a set, so that for each row every element must appear once
            for j in range(9):
                item = board[i][j]
                if item in s: # if the item is already in the set, return false
                    return False
                elif item != '.': # if the item is not in set and is not a period, add it in the set
                    s.add(item)


        # Validate Columns
        for i in range(9):
            s = set() # make a set, so that for each column every element must appear once
            for j in range(9):
                item = board[j][i]
                if item in s:  # if the item is already in the set, return false
                    return False
                elif item != '.': # if the item is not in set and is not a period, add it in the set
                    s.add(item)

        # Validate Boxes
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)] # all the possible boxes in the sudoku

        for i, j in starts: # for all i, j pairs in the starts
            s = set() # make a set, so that for each column every element must appear once
            for row in range(i, i+3): #since every box is of width 3
                for col in range(j, j+3): #since every box is of height 3
                    item = board[row][col]
                    if item in s:  # if the item is already in the set, return false
                        return False
                    elif item != '.': # if the item is not in set and is not a period, add it in the set
                        s.add(item)

        # if we reach here, that means we satisfy all the conditions, so we return true
        return True

# Time: O(n^2)
# Space: O(1) {Since we store at max 9 items}