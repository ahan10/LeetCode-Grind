# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mul = 1 # the left multiplicand initially is at the i-1 index, that is just outside the range
        r_mul = 1 # the right multiplicand initially is at the i+1 index, that is just outside the range

        n = len(nums)

        # make two 0 arrays of length n

        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n): # iterating from left to right, i is the index from left
            j = -i - 1 # -ve indexed in python is the index from right, so negative of the current index from left, minus one give the current index from right

            l_arr[i] = l_mul # the current left multiplicand becomes the value of multiplication of the elements to left of the current ones
            r_arr[j] = r_mul # the current right multiplicand becomes the value of multiplication of the elements to right of the current ones

            l_mul *= nums[i] # update the left multiplicand with the current i element as in the next iteration we will move right
            r_mul *= nums[j] # update the right multiplicand with the current j element as in the next iteration we will move left

        return [l*r for l, r in zip(l_arr, r_arr)] # return a new array as the multiplication of the same index of both left and right array

# Time: O(n)
# Space: O(n)