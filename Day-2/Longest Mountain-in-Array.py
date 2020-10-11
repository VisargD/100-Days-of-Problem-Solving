"""
Problem Name: Longest Mountain In Array
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/longest-mountain-in-array/
"""


class Solution:
    def longestMountain(self, A: List[int]) -> int:

        # count tracks the latest mountain size. maxi tracks the maximum mountain size at any point in loop.
        count = 0
        maxi = 0

        # Using for loop from 1 to len(A) - 1 to find local highest points in any array.
        for i in range(1, len(A) - 1):

            # Any point is local highest if it is greater than its surrounding values.
            if A[i - 1] < A[i] > A[i + 1]:

                # If local highest is found, then its left and right part should be in descending order from the highest ppint.
                # So set left and right index for further calculation.
                # Here, count is set to 3 as the local highest and its surrounding values are already forming a mountain.
                left_index = i - 1
                right_index = i + 1
                count = 3

                # Go through the left part of highest point and count until the descending order is maintained.
                # This means count until the element value keeps decreasing and stop as soon as it increases.
                while left_index > 0:
                    if A[left_index] > A[left_index - 1]:
                        count += 1
                        left_index -= 1
                    else:
                        break

                # Go through the right part of highest point and count until the descending order is maintained.
                # This means count until the element value keeps decreasing and stop as soon as it increases.
                while right_index < len(A) - 1:
                    if A[right_index] > A[right_index + 1]:
                        count += 1
                        right_index += 1
                    else:
                        break

            # After every iteration, check the maximum out of current count and the maxi value.
            maxi = max(maxi, count)

        # Return the maximum mountain value.
        return maxi
