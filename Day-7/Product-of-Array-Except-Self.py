"""
Problem Name: Product of Array Except Self
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/product-of-array-except-self/
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # This is a simple approach in which we iterate through the array for two times.
        # In the first loop, we calculate the product for the left part of the value.
        # In the second loop, we calculate the product for the right part of the value.
        # And finally we multiply both of them.

        # The left and right product for first and last element respectively will always be 1 as they are no element on left and right side respectively.
        # So, inital 2 arrays of length of nums.
        # One will store the product of left part of all the elements.
        # And the other will store the product of right part of all elements.
        product_of_left = [1] * len(nums)
        product_of_right = [1] * len(nums)
        answer = []

        # Using for-loop to iterate from second to last element.
        # For every element, find product of all preceding elements.
        for i in range(1, len(nums)):
            product_of_left[i] = product_of_left[i - 1] * nums[i - 1]

        # Using for-loop to iterate from second-to-last element to first element.
        # For every element, find product of all succeeding elements.
        for j in reversed(range(len(nums) - 1)):
            product_of_right[j] = nums[j + 1] * product_of_right[j + 1]

        # Product of all element except itself is simply the product of element before and after the element.
        # Product of elements before any value is stored in product_of_left.
        # Product of elements after any value is stored in product_of_right.
        # So simply multiply both and append product in answer list.
        for k in range(len(nums)):
            answer.append(product_of_left[k] * product_of_right[k])

        # Return the answer list.
        return answer
