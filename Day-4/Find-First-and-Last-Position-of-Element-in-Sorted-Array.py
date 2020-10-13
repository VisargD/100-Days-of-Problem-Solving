"""
Problem Name: Find First and Last Position of Element in Sorted Array
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Initializing start and end to -1 to return [-1,-1] if target is not present in array.
        start = -1
        end = -1

        # Using for loop to traverse through the list.
        for i in range(len(nums)):

            # Check if current value is equal to target.
            # If yes, then set start and end to current index and set index (i) to the next position.
            # And then use while loop to check the end position of target in array.
            if nums[i] == target:
                start = i
                end = i
                i += 1

                # Use while to keep the index inside the bounds.
                while i != len(nums):

                    # If the current value is not equal to target then return the last found start and end value.
                    if nums[i] != target:
                        return [start, end]

                    # If current value matches to target but is the last element then,
                    # Increment end and return [start, end]  as there is no value after the last index.
                    elif i == len(nums) - 1:
                        end += 1
                        return [start, end]

                    # If current value is equal to target and it is also not the last element of array then,
                    # Increment end and increment index to check the next element in array.
                    elif nums[i] == target:
                        end += 1
                        i += 1

        # If target is not found in the array, then it will return the default [-1, -1] value.
        return [start, end]
