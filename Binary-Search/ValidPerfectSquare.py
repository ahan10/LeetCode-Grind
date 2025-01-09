# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 1, num # 2 pointers min can be 1 and max can be number itself

        while l <= r: # binary search
            m = (l + r) // 2 # middle value
            square = m ** 2 # square of the middle value

            if square == num: # if square is our target we found it
                return True
            elif square > num: # if square is bigger than the num, then the number potentially lies between left and middle
                r = m - 1
            else: # if square is smaller than the num, then the number potentially lies between middle right
                l = m + 1

        # at the end if we exit the loop, meaning we found nothing, we return false
        return False

    # Time: O(n)
    # Space: O(1)