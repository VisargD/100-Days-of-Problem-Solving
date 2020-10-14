"""
Problem Name: Implement strStr()
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Initializing i, j and count to 0.
        # This is a simple 2 pointer approach that uses while-loop where i is used in haystack and j in needle.
        # start keeps track of the starting index of needle occurence in haystack.
        count = 0
        i = 0
        j = 0
        start = 0

        # Checking the case where needle is empty.
        if needle == "":
            return 0

        # Using while-loop until i reaches the last index.
        while i != len(haystack):

            # If the element at current index i and j in both the strings are same then,
            # Increment count, i and j. Here count keeps track of number of words in needle that are currently matching.
            if haystack[i] == needle[j]:
                start = i - count
                count += 1
                j += 1
                i += 1

                # If count is equal to len(needle), it means that all the characters of needle have occured in sequence in haystack string.
                # So, return the start index.
                if count == len(needle):
                    return start

            # If the elements in both the array does not match then,
            # Refresh the count and j (pointer for needle) to 0.
            # Then increment the i and start value to the next value from current position.
            else:
                count = 0
                j = 0
                i = start + 1
                start += 1

        # If needle string is not found in haystack then return -1.
        return -1
