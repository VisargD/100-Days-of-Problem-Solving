"""
Problem Name: Find Minimum in Rotated Sorted Array
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initializing low and high to first and last index respectively.
        low = 0
        high = len(nums) - 1

        # Using while-loop to perform iterative binary search.
        while high > low:

            # Calculating mid for each iteration.
            mid = (low + high) // 2

            # If value at mid is greater than value at high, then the pivot element is on the right side of mid.
            # Set low to mid + 1 to perform binary search in the right side.
            if nums[mid] > nums[high]:
                low = mid + 1

            # If the value at mid is lower than value at high, then either the value at mid can be pivot or the pivot can be in the left part of mid.
            # Set high = mid to search in the left part.
            # Here, it is not possible to set high = mid - 1 as the value at mid can also be a pivot element.
            else:
                high = mid

        # When the above loop breaks, then high will be equal to low. And that will be the required pivot element.
        # There are no more possibilities of pivot being on the left or right as high is equal to low.
        # So return it.
        return nums[low]
