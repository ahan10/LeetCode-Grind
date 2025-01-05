# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/

# not the optimal but hte most trivial solution

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        ans = []

        i, j = 0, 0 # indexes of the row and column

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3 # integers associated to the direction
        direction = RIGHT # initially we move right

        # out of bounds for the walls

        UP_WALL = 0 # up wall is the 0th row
        RIGHT_WALL = n # right wall is the nth column
        DOWN_WALL = m # down wall is the mth row
        LEFT_WALL = -1 # left wall is the -1st column

        while len(ans) != m * n: # we have traversed the matrix once the length of the array is equal to the length of the matrix
            if direction == RIGHT: # if we are moving in the right direction
                while j < RIGHT_WALL: # until we hit the right wall
                    ans.append(matrix[i][j]) # append the current element of the
                    j += 1 # and move more right
                i, j = i + 1, j - 1 # once we hit the wall, i+1 means we move a row down; j - 1, we get j back in the index
                RIGHT_WALL -= 1 # pinch the right wall in, as we do not want to look at those elements again
                direction = DOWN    # once we are done with moving right, we move down

            elif direction == DOWN: # if we are moving in the down direction
                while i < DOWN_WALL: # until we hit the right wall
                    ans.append(matrix[i][j]) # append the current element of the
                    i += 1 # and move more down
                i, j = i - 1, j - 1 # once we hit the wall, i-1, we get i back in the index; j - 1, we start with the (j - 1)th index as we have covered till index j
                DOWN_WALL -= 1 # move the down wall up
                direction = LEFT # once we are done with moving down, we move left

            elif direction == LEFT: # if we are moving in the down direction
                while j > LEFT_WALL: # until we hit the left wall
                    ans.append(matrix[i][j]) # append the current element of the
                    j -= 1 # and move more left
                i, j = i - 1, j + 1 # once we hit the wall, i-1, we move i to a row above; j - 1, we get j back in the index
                LEFT_WALL += 1 # move left wall to right, pinching it
                direction = UP # once we are done with moving left, we move up

            else: # the last direction left is up
                while i > UP_WALL: # until we hit the up wall
                    ans.append(matrix[i][j]) # append the current element of the
                    i -= 1 # and keep moving up
                i, j = i + 1, j + 1 # once we hit the wall, i+1, we get i back in index; j + 1, we move j to the right
                UP_WALL += 1 # pinch the up wall in
                direction = RIGHT # switch the direction to right

        return ans

# Time: O(n*m)
# Space: O(1) (if we do not include the output array)
# Space: O(n*m) if we include the output array