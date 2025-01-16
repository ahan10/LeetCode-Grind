# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

# for this one, we will go from back to front, we will compare which is the bigger number and place it at the end

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y = m-1, n-1

        for z in range(m + n - 1, -1, -1): # m + n - 1: total size of nums1; -1: decrement by -1 and last -1 is loop till 0 since it is exclusive
            if x < 0: # x < 0 means we have traversed the whole nums1; and we simply append nums 2
                nums1[z] = nums2[y]
                y -= 1
            elif y < 0: # this means we have traversed the nums2, and since nums 1 is sorted, we do not want to proceed any further
                break
            elif nums1[x] > nums2[y]: # if the number at x in nums 1 > number at y in nums 2; we want to append x at nums 1 at z at nums 1
                nums1[z] = nums1[x]
                x -= 1
            else: # else we want to append y at nums 2 to z at nums1
                nums1[z] = nums2[y]
                y -= 1

        # since we had to do it in place, we do not return anything

    # Time: O(n + m)
    # Space: O(1)