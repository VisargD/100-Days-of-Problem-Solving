"""
Problem Name: Search Insert Position
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Initialize position to 0.
        position = 0

        # Using for-loop to iterate through the list.
        for i in range(len(nums)):

            # If value at i is target then simply return the index i.
            if nums[i] == target:
                return i

            # As the list is in ascending order, target can't be placed after a larger value.
            # So if value is larger than target then return the current position value.
            if nums[i] > target:
                return position

            # If the current value at index is not target and it is smaller than target then increment position.
            else:
                position += 1

        # If the target is greater than the last value of list then no value will be returned in the above loop.
        # For such cases, the target needs to be placed at position after last element of list.
        # After for-loop position will have value of len(nums). So return it.
        return position
