"""
Problem Name: Find All Numbers Disappeared in an Array
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


"""
APPROACH:
It is stated that all the values of list will be between 1 and n (size of list).
So it is possible to map a value to (value - 1) index. E.g.: 1 can be mapped to 0 index. 2 can be mapped to 1 index.
For every value, set the nums[abs(value) - 1] value to negative, if it is positive currently.
If the value is already negative then it means that the value has occured already.
If after the above two steps any positive value is found at any index then index+1 can be considered as disappeared value.

EXAMPLE:
Input: [4,3,2,2,1]
Iteration will look like this:
    1. Check if the value at nums[abs(4) - 1] = nums[3] is negative. If not then multiply nums[3] with -1. (AFTER: [4,3,2,-2,1])
    2. Check if the value at nums[abs(3) - 1] = nums[2] is negative. If not then multiply nums[2] with -1. (AFTER: [4,3,-2,-2,1])
    3. Check if the value at nums[abs(2) - 1] = nums[1] is negative. If not then multiply nums[1] with -1. (AFTER: [4,-3,-2,-2,1])
    4. Check if the value at nums[abs(2) - 1] = nums[1] is negative. It is negative so 2 is repeating. No changes to do. (AFTER: [4,-3,-2,-2,1])
    5. Check if the value at nums[abs(1) - 1] = nums[0] is negative. If not then multiply nums[0] with -1. (AFTER: [-4,-3,-2,-2,1]) 
    6. Now loop through the modified array and if value at any index is positive then it means that (index+1) value was not found during above process.
    7. Here, the value at last index(4) is positive. So index+1 ,i.e, 5 is the disappeared number which is actually the correct answer.   
    8. Add the values to the 'disappeared' list and return it.
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Creating an empty list to add all the disappeared values later.
        disappeared = []

        # Looping through all the values of 'nums' list.
        for x in nums:

            # Check if the value at nums[abs(x) - 1] is negative.
            # If yes, then it means it has already occured once.
            # If no, then it is occuring for the first time. So multiply nums[abs(x) - 1] with -1 to make it negative.
            if nums[abs(x) - 1] > 0:
                nums[abs(x) - 1] *= -1

        # Array will be modified after the above loop.
        # Now check if value at any index is negative. If found then (index + 1) will be one of the disappeared number.
        # Add it to the list.
        for i in range(len(nums)):
            if nums[i] > 0:
                disappeared.append(i+1)

        # Return the final 'disappeared' list.
        return disappeared
