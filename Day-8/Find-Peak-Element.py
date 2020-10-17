"""
Problem Name: Find Peak Element
Platform: Leetcode
Difficulty: Medium
Platform Link: https://leetcode.com/problems/find-peak-element/
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Check if there is only one element in the array.
        # As mention in the problem statement, nums[-1]=nums[n]=(- infinity).
        # So if there is only one element, then it will itself be a peak. Return first index (0) in this case.
        if len(nums) == 1:
            return 0

        # Using for-loop to iterate through the list.
        for i in range(len(nums)):

            # If it is the first element then check if it is greater than the 2nd element.
            # If yes, then return the current index.
            # Keep in mind that nums[-1] is (minus infinity). So we only need to compare the next element.
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i

            # If it is the last element then check if it is greater than last-second element.
            # If yes, then current value is peak value. Return the index.
            # Keep in mind that nums[n] is (minus infinity). So we only need to compare the previous element.
            elif i == len(nums) - 1:
                if nums[i] > nums[i - 1]:
                    return i

            # If the number is between the first and last element then check if it is greater than both the neighbors.
            # If yes, then return the index.
            elif nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
