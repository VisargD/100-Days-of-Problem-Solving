"""
Problem Name: Find All Numbers Disappeared in an Array
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


"""
APPROACH: 
The problem states that a list containes value ranging from 1 to length but few are repeating twice, once or are not present in the list at all. 
If any value from 1 to length(nums) is not present in the list then it is considered as disappeared.
This approaches uses set. The input list is converted to set so that all the duplicates are removed.
Then loop from 0 to len(nums) and check if i+1 is present in the set. (This will check which of the 1 to length(nums) values are not present).
If it is present then it means that it is not the disappeared number.
Here, i+1 is used because index is starting from 0 and the value are between 1 and length (inclusively). So everytime i+1 is checked.
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Creating a set from the 'nums' list so that all the duplicates are removed.
        num_set = set(nums)

        # Creating an empty list to store the disappeared value later.
        disappeared = []

        # Looping from i = 0 to len(nums)-1 (Inclusive).
        # As the problem states that the values of the list are between 1 and length of list (Inclusive).
        # So if at any point i+1 is not present in the set, we can mark it as disappeared.
        for i in range(len(nums)):

            # If i+1 is not present in the set then it means that the number is one of the disappeared number.
            # Add it to the 'disappeared' list.
            if i+1 not in num_set:
                disappeared.append(i+1)

        # Return the final disappeared list.
        return disappeared
