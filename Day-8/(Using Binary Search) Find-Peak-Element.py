"""
Problem Name: Find Peak Element
Platform: Leetcode
Difficulty: Medium
Platform Link: https://leetcode.com/problems/find-peak-element/
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # The basic intuition behind this approach is that if an element is greater than its next element then,
        # the element is on the path from peak (local maximum) towards a lower value (local minimum) and,
        # If the element is smaller than the next element then,
        # the element is on the path from a lower value (local minimum) towards a peak (local maximum).

        # Initializing low and high to first and last position respectively.
        low = 0
        high = len(nums) - 1

        # Using while-loop to perform iterative binary search.
        while low < high:

            # Calculating mid value on every iteration.
            mid = (low + high) // 2

            # If value at mid is greater than next value then it means that the point comes in-between a path from peak going towards a local minimum.
            # This value can also be the peak itself. So don't set high to mid+1 as current element can also be a peak.
            # So search in the left part.
            if nums[mid] > nums[mid + 1]:
                high = mid

            # If value at mid is lower than next value then it means that the point comes in-between a path from local minimum going towards peak.
            # So search for the peak in the right side.
            else:
                low = mid + 1

        # The loop will break when low will become equal to high which will be the required answer. Return the index.
        return low


# Here, any one of the peaks needs to be return so we can return index of any local minimum.
# There is no requirement of the peak being a global maximum.
