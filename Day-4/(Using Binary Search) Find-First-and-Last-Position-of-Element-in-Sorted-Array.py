"""
Problem Name: Find First and Last Position of Element in Sorted Array
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Helper function to perform recursive Binary Search.
        def binary_search(nums: List[int], low: int, high: int, target: int) -> List[int]:

            # Initializing start and end to -1 to return [-1,-1] if target is not present in array.
            start = -1
            end = -1

            # If the high index is higher than or equal to low index then set mid index using the formula.
            if high >= low:
                mid = (high + low) // 2

                # If the value at mid is equal to target then set start and end index to mid index.
                # And set index (i) to mid - 1 to search in the left side from mid to find the starting point.
                if nums[mid] == target:
                    start = mid
                    end = mid
                    i = mid - 1

                    # This while loop searches the left part from mid to find the start position of target.
                    while i != -1:

                        # If current is not equal to target then break from loop because there is no point in continuing.
                        if nums[i] != target:
                            break

                        # If we reached the first element and it is equal to target then update start and break while-loop.
                        elif i == 0:
                            start -= 1
                            break

                        # If the current value matches target and it is not first element then,
                        # Simply update start and set index to the next left index (decrement).
                        elif nums[i] == target:
                            start -= 1
                            i -= 1

                    # Now set index (i) to mid + 1 to search in the right side to find the end position.
                    # This while loop searches the right part from mid to find the end position of target.
                    i = mid + 1
                    while i != len(nums):

                        # If current is not equal to target then break from loop because there is no point in continuing.
                        if nums[i] != target:
                            break

                        # If we reached the last element and it is equal to target then update end and break while-loop.
                        elif i == len(nums) - 1:
                            end += 1
                            break

                        # If the current value matches target and it is not last element then,
                        # Simply update end and set index to the next right index (increment).
                        elif nums[i] == target:
                            end += 1
                            i += 1

                    # Finally return the updated [start, end] value.
                    return [start, end]

                # If value at mid is greater than target then perform binary search on left side.
                # Set high = mid - 1.
                elif target < nums[mid]:
                    return binary_search(nums, low, mid - 1, target)

                # If value at mid is smaller than target then perform binary search on right side.
                # Set low = mid + 1.
                else:
                    return binary_search(nums, mid + 1, high, target)

            # If target not found in array then return default [-1,-1] value.
            else:
                return [start, end]

        # Call the binary search helper function on nums list with low = 0 and high = len(nums)-1.
        return binary_search(nums, 0, len(nums) - 1, target)
