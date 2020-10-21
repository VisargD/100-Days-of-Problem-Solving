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

            # If x is already present in the dictionary as a key, then it means that it is repeating.
            # So, increment the value of the x in the dictionary by 1.
            if x in hash_table:
                hash_table[x] += 1

            # If x is not present in the dictionary, then it means that it occured for the first time.
            # So set its value to 1.
            else:
                hash_table[x] = 1

        # After the dictionary is populated with frequency of all the values of the 'nums' list,
        # Check for the key whose value is equal to 2 (i.e, occurs twice).
        # If found then add it to the 'duplicates' list.
        for key in hash_table:
            if hash_table[key] == 2:
                duplicates.append(key)

        # Return the duplicates list that contains all the value that occured twice.
        return duplicates
