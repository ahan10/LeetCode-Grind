# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {} # make a counter or use the Counter() function form the collections
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        maxCount = -1 # max count is -1 since we compare it
        ans = -1 # max count is -1 and we will update it later on

        for key, value in counter.items(): # for each key value pair in the dict
            if value > maxCount: # if the current value is greater than the max count; then update hte max count and the value
                maxCount = value
                ans = key

        return ans

# Time: O(n)
# Space: O(n)

# Solution with Time O(n) but Space O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None # candidate is none
        count = 0 # current count is 0

        for num in nums: #iterate over the nums
            if count == 0: # if teh count is 0, the current element becomes the candidate
                candidate = num

            if candidate == num: # if the current num is candidate, increment the count
                count += 1
            else: # else, decrement the count
                count -= 1

        # since it is guaranteed that the majority element is n//2 times present, we will have the count at least 1; and it becomes our majority element
        return candidate

# Time: O(n)
# Space: O(1)