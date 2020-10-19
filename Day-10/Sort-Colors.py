"""
Problem Name: Sort Colors
Platform: Leetcode
Difficulty: Medium
Platform Link: https://leetcode.com/problems/sort-colors/
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Initializing color_0, color_1 and color_2 to 0
        # color_0 represents red color and it will store total occurences of red color in the nums list.
        # color_1 represents white color and it will store total occurences of white color in the nums list.
        # color_2 represents blue color and it will store total occurences of blue color in the nums list.
        color_0 = 0
        color_1 = 0
        color_2 = 0

        # This for-loop will count the number of red, white and blue occurences in the list.
        for i in range(len(nums)):

            # If the digit is 0 then it means that the color is 'red'.
            # Increment color_0 counter.
            if nums[i] == 0:
                color_0 += 1

            # If the digit is 1 then it means that the color is 'white'.
            # Increment color_1 counter.
            elif nums[i] == 1:
                color_1 += 1

            # If the digit is 2 then it means that the color is 'blue'.
            # Increment color_2 counter.
            else:
                color_2 += 1

        # The basic idea behind this approach is to first count the number of red, white and blue.
        # Then modify the first count_0 number of values to 0. Then change the remaining count_1 number of values to 1.
        # And then change the remaining count_2 number of values to 2.
        # This will modify the input list into sorted list of color (all the red --> all the white --> all the blue).
        for i in range(len(nums)):

            # Until color_0 counter is not 0, modify the list values to 0 (i.e, red).
            if color_0 != 0:
                nums[i] = 0
                color_0 -= 1

            # After all the 'red' are placed in their position, move on to place the 'white' color.
            # Until color_1 counter is not 0, modify the list values to 1 (i.e., white).
            elif color_1 != 0:
                nums[i] = 1
                color_1 -= 1

            # After all the 'white' are placed in their position, move on to place the 'blue' color.
            # Until color_2 counter is not 0, modify the list values to 2 (i.e., blue).
            else:
                nums[i] = 2
                color_2 -= 1
