"""
Problem Name: Sort Colors
Platform: Leetcode
Difficulty: Medium
Platform Link: https://leetcode.com/problems/sort-colors/
"""

"""
APPROACH:
In this approach, 3 pointers will be used.
Initially zero_index will point to the first index (beginning) of list and two_index will point to the last index (end).
In order to sort the color list, we need all the 0's in the beginning, all the 2's in the end and all 1's in-between.
Everytime a 0 will be found it will be swapped with value at zero_index and then zero_index will be incremented by 1.
By doing this, all the 0's will be placed in the beginning starting from 0 index.
Everytime a 2 will be found it will be swapped with value at two_index and then two_index will be decremented by 1.
By doing this all the 2's will be placed in the end. So 1's will be in the middle.
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Function to perform swapping using index.
        def swapValue(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        # Initializing zero_index and index to 0 and two_index to the last index as explained earlier.
        zero_index = 0
        two_index = len(nums) - 1
        index = 0

        # Using while loop until index is less than or equal to two_index.
        while index <= two_index:

            # If the current value is 0 then swap it with zero_index value.
            # Increment zero_index to store the next 0 whenever found.
            # Increment the index.
            if nums[index] == 0:
                swapValue(nums, index, zero_index)
                zero_index += 1
                index += 1

            # If the current value is 2 then swap it with two_index value.
            # 2's will be placed from the end so after every swap the two_index needs to be decremented to store the next 2 whenever found.
            # Here index is not incremented because the swapped value may not be in its correct position. So it needs to be checked again.
            elif nums[index] == 2:
                swapValue(nums, index, two_index)
                two_index -= 1

            # If the current value is 1 then no need to swap it as we need 1's in the middle for the sorted list.
            # Simply increment the index.
            else:
                index += 1

# In the end, the modified list will have this form:
#       Index Range:
#           (0 -> zero_index - 1) (Inclusive):                filled with 0's
#           (zero_index -> index - 1) (Inclusive):            filled with 1's
#           (two_index + 1 -> len(nums) - 1) (Inclusive):     filled with 2's
