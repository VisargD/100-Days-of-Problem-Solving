"""
Problem name: Move Zeros
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/move-zeroes/
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Using index and count to keep track of array index and the number of while loop iterations respectively.
        index = 0
        count = 0

        # Using a while loop to iterate one less than length of array times (one less because index starts from 0).
        while count < len(nums):

            # If the value at index is 0 then pop the value and append 0 to the array.
            # Here, index is not incremented because after popping the 0, all the remaining elements will shift to the left by 1.
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                count += 1

            # If value at index is not 0 then simply increment count and index.
            else:
                index += 1
                count += 1

        # Return the modified array.
        return nums
