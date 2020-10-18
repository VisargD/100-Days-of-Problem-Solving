"""
Problem Name: Longest Substring Without Repeating Characters
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # start_index will store the starting position from where non-repeating elements have occured in sequence.
        # hash_table will store the latest index of values present in the string.
        # maxi will store the value of maximum length non-repeating sub-string at every iteration of loop.
        start_index = 0
        hash_table = {}
        maxi = 0

        # Using for-loop to iterate through the string.
        for i in range(len(s)):

            # If the current character is present in the dictionary then it means that it is repeating.
            # Change the start index to maximum of current start index and index value of current character stored in the dictionary.
            # Change the index of the character in the dictionary to the current index.
            # Update the maximum value by comparing current maxi value and the current length of non-repeating sequence from start index (i - start_index + 1).
            if s[i] in hash_table:
                start_index = max(start_index, hash_table[s[i]] + 1)
                hash_table[s[i]] = i
                maxi = max(maxi, i - start_index + 1)

            # If the character is not present in the dictionary then add the character along with its index.
            # Update the maximum value by comparing current maxi value and the current length of non-repeating sequence from start index (i - start_index + 1).
            else:
                maxi = max(maxi, i - start_index + 1)
                hash_table[s[i]] = i

        # Return the final maximum value.
        return maxi
