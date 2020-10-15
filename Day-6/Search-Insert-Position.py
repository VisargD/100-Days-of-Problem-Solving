"""
Problem Name: Search Insert Position
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Initializing high and low index to first and last to perform binary search.
        high = len(nums) - 1
        low = 0

        # Using while loop until high is more than or equal to low. (Iterative Binary Search)
        while high >= low:

            # Calculating mid at every iteration.
            mid = (high + low) // 2

            # If the value at mid is target then simply return the index.
            if nums[mid] == target:
                return mid

            # If target is smaller than current value at mid then search in the left part. (Because input list is sorted)
            # Set high to mid - 1 to search in the left side.
            elif target < nums[mid]:
                high = mid - 1

            # If target is larger than current value at mid then search in the right part. (Because input list is sorted)
            # Set low to mid + 1 to search in the right side.
            else:
                low = mid + 1

        # If at any point, high becomes smaller than low then simply return the last updated low value.
        return low
