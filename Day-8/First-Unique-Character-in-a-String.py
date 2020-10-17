"""
Problem Name: First Unique Character in a String
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/first-unique-character-in-a-string/
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Using a dictionary to keep track of count of every element in string.
        hash_table = {}

        # Using for-loop to iterate through the the characters of the string.
        for i in range(len(s)):

            # If the character is already in the dictionary then it means that it has been repeated.
            # So mark the value as repeated by making its value equal to -1.
            if s[i] in hash_table:
                hash_table[s[i]] = -1

            # If the character is not present in the dictionary then it means that the character is occuring for the first time.
            # So add the character along with its index as value.
            else:
                hash_table[s[i]] = i

        # After the above loop, the dicitionary will be populated with all the characters of string along with their frequency.
        # If the value is -1, then it means that the character is repeated.
        # This for-loop will return index of the first character that is not repeated.
        for x in hash_table:

            # Check if value for key in dictionary is -1.
            # If the value is not -1 then the character is a unique one.
            # Return the first index at which the value is not -1.
            if hash_table[x] != -1:
                return hash_table[x]

        # If no unique character is found then return -1.
        return -1
