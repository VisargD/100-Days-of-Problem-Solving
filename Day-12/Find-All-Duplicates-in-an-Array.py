"""
Problem Name: Find All Duplicates in an Array
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # Creating a dictionary to store the frequency of each value present in the list.
        hash_table = {}

        # Creating an empty list to store the duplicates that occur twice.
        duplicates = []

        # Looping through all the values of the 'nums' list
        for x in nums:

            # As the problem states, all the values either occur once or twice only and not more than that.
            # If x is in the dictionary then it means that the number has already occured once and it is repeating now.
            # So add x to the 'duplicates' list.
            if x in hash_table:
                duplicates.append(x)

            # If x is not present in the dictionary then it means that it is occuring for the first time.
            # So set its value to 1.
            else:
                hash_table[x] = 1

        # Return the 'duplicates' list which will contains all the values that occured twice.
        return duplicates
