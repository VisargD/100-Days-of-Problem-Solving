"""
Problem Name: Implement strStr()
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # This is simple approach that uses built-in function.
        # If needle is empty string then return 0.
        if needle == "":
            return 0

        # Check if needle is in haystack using the "in" operator anf return the index.
        if needle in haystack:
            return haystack.index(needle)

        # If not found then return -1.
        return -1
