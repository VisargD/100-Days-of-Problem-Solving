"""
Problem Name: Implement strStr()
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/implement-strstr/
"""

# This solution uses KMP Approach.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Storing the length of needle and haystack string.
        needle_length = len(needle)
        hay_length = len(haystack)

        # This helper function finds lps array (Longest prefix which is also a suffix) for needle string.
        def kmp_helper(needle):

            # Initialize lps list with first element as 0 as there is no prefix of first element.
            # Initialize i and j for needle string to implement two pointer for finding prefix.
            # j points to first index and j points to second index.
            lps = [0]
            j = 0
            i = 1

            # Using while-loop until i reaches last index.
            while i < needle_length:

                # If element at i and j is same then increment both pointers to check the next elements.
                # Assign or append (j + 1) as the elements are matching so this will increment prefix length.
                if needle[i] == needle[j]:
                    lps.append(j + 1)
                    j += 1
                    i += 1

                # If the element does not match then change the j value to lps[j - 1].
                # Do not change the j value directly to 0 as the value of lps shows the maximum length prefix which is also a suffix.
                # Eventually if nothing matches then j will become 0.
                elif j != 0:
                    j = lps[j - 1]

                # If j is 0 then simply append 0 to lps and increment i to move to the next index.
                # lps stores the length maximum matching prefix which is also a suffix upto that index.
                else:
                    lps.append(0)
                    i += 1

            # Return the lp list.
            return lps

        # This function performs he KMP string matching and uses the above function.
        def kmp(haystack, needle):

            # Check the cases where either needle is empty or needle is greater than haystack string.
            if needle_length == 0:
                return 0
            if hay_length - needle_length < 0:
                return -1

            # Call the lps helper function and store the list.
            # Initialize 2 pointers for haystack and needle.
            lps = kmp_helper(needle)
            i = 0
            j = 0

            # Use while-loop until index reaches the last position.
            while i < hay_length:

                # If element in needle and haystack matches then simply increment both the pointers.
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1

                # If elements do not match and j is not yet 0 then set j to lps[j-1] to check if the element matches.
                # Eventually if it does not match then j will become 0 ,i.e., it will reach the 1st position of needle.
                elif haystack[i] != needle[j] and j != 0:
                    j = lps[j-1]

                # If j is 0 then it has reached the first element of needle so no match was found in between.
                # Increment i.
                else:
                    i += 1

                # If j becomes equal to needle length then it means that all the characters of needle were found in sequence in haystack.
                # If this happens then deduct needle length from i to find the starting index from where the matching started.
                if j == needle_length:
                    return i - needle_length

            # If no match is found then return -1.
            return -1

        # Call the above function to perform matching and return the result.
        return kmp(haystack, needle)
