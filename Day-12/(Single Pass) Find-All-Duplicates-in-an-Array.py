"""
Problem Name: Find All Duplicates in an Array
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


"""
APPROACH:
It is stated that all the values of list will be between 1 and n (size of list).
So it is possible to map a value to (value - 1) index. E.g.: 1 can be mapped to 0 index. 2 can be mapped to 1 index.
For every value, set the nums[abs(value) - 1] value to negative, if it is positive currently.
If the value is already negative then it means that the value has occured already. So add it to duplicate list.

EXAMPLE:
Input: [2,1,1,3]
Iteration will look like this:
    1. Check if the value at nums[abs(2) - 1] = nums[1] is negative. If not then multiply nums[1] with -1. (AFTER: [2,-1,1,3])
    2. Check if the value at nums[abs(1) - 1] = nums[0] is negative. If not then multiply nums[0] with -1. (AFTER: [-2,-1,1,3])
    3. Check if the value at nums[abs(1) - 1] = nums[0] is negative. It is negative which means that it is repeating. Add 1 to the duplicate list (AFTER: [-2,-1,1,3])
    4. Check if the value at nums[abs(3) - 1] = nums[2] is negative. If not then multiply nums[2] with -1. (AFTER: [-2,-1,-1,3]) 
    5. So duplicate list will only contain 1.
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # Creating a list to store all the values that will occur twice.
        duplicates = []

        # Loop through all the values present in 'nums' list.
        for value in nums:

            # If the value at nums[abs(value) - 1] is negative then it means the value is repeating as discussed above.
            # So add it to the duplicates list.
            if nums[abs(value) - 1] < 0:
                duplicates.append(abs(value))

            # If value at nums[abs(value) - 1] is not negative then make it negative by multiplying it by -1.
            # So that next time if the same element occurs then it can be added to duplicates list.
            else:
                nums[abs(value) - 1] *= -1

        # Return the duplicates list.
        return duplicates
