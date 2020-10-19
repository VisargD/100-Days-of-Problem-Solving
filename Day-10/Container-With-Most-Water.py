"""
Problem Name: Container With Most Water
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/container-with-most-water/
"""


"""
INTUITION:

The basic intuition behind this approach is that on every iteration width of the container will surely decrease.
So in order to compensate this decrease in width, greater height will be required.
So at every step, update the max value and then move the shorter bar in hope that a greater height will be obtained.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Initializing maximum, i, j and floor length.
        # i and j will represent the left and right bar of the container respectively.
        # floor will represent the width of the container (Initially length(height) - 1).
        maxi = 0
        i = 0
        j = len(height) - 1
        floor = len(height) - 1

        # Using while-loop to stop left and right bar of container from crossing each other.
        while i < j:

            # Checking and updating max value in every iteration with the maximum are.
            # Area = shorter height * floor. It is only possible to fill upto shorter height otherwise water will overflow.
            maxi = max(min(height[i], height[j]) * floor, maxi)

            # On every iteration, floor height will decrease by 1 as one of the bar of container will move.
            floor -= 1

            # Everytime move the smaller bar in hope that a larger bar will occur next.
            # If left bar is higher than the right bar then move the right index towards left side (decrement).
            if height[i] > height[j]:
                j -= 1

            # If left bar is smaller than right bar then move the left index towards right side (increment).
            else:
                i += 1

        # Return the final maximum area obtained.
        return maxi
