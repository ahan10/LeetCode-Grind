# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k): # we want a function to see if the hour rate k, we found works
            hours = 0 # initially 0 hours
            for p in piles: # iterate over all the stacks in the pile
                hours += ceil(p / k) # hour to eat a stack is the ceiling value that you get after dividing the number of bananas in a stack by the rate per hour

            return hours <= h # if the time taken to eat is less than or equal to the time guards are not around then it is valid

        l, r = 1, max(piles) # we now perform a binary search over the least amount of time and the max amount of time

        while l < r: # we do not want them to equal to each other since we run in an infinite loop
            k = (l + r) // 2 # middle index
            if k_works(k): # if k works, we know the values after k work too
                r = k # since we don't know k - 1 works we move right to k as we are guaranteed that it is current minimum
            else: # else if k does not work, we know all the values upto k don't work so we go 1 ahead of k
                l = k + 1

        return l # at the end l = r so return any of it

# Time: O(n*log(max(piles)))
# Space: O(1)