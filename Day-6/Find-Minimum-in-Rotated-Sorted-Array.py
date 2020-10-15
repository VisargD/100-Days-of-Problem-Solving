"""
Problem Name: Find Minimum in Rotated Sorted Array
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Start a loop from 1 to last index.
        for i in range(1, len(nums)):

            # The pivot point from where the rotation is separated must be smaller than previous element.
            # E.g.: [4,5,6,7,0,1,2]. Here pivot element is 0 which is smaller than previous element.
            # If this happend, then simply return this element.
            if nums[i] < nums[i-1]:
                return nums[i]

        # This return statement comes into when list only contains one element or when everything is already in order.
        # E.g. [1, 2]. In such case, simply return first element.
        return nums[0]
