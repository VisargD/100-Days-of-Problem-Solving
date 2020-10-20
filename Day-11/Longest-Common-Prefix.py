"""
Problem Name: Longest Common Prefix
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/longest-common-prefix/
"""


"""
APPROACH:
Initially, longest common prefix is the first word of the list.
Then second word is compared with 'common' character-by-character. 'common' is updated with only the part that matches.
This updated 'common' is then used to match with the third word. And the same process is then followed everytime.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # If no words are present in the 'strs' list then return empty string as longest common prefix. (i.e., an empty list)
        if len(strs) == 0:
            return ""

        # Initialize common prefix to the first word of the list.
        common = strs[0]

        # Iterate through all the words of the 'strs' list.
        for x in strs:

            # Initialize index to 0 to match each word with 'common' prefix everytime.
            i = 0

            # Using while-loop to match each character of the current word with each character of 'common' one-by-one.
            # If at any point the character does not match, then simply break this while-loop.
            while i < len(common) and i < len(x):
                if x[i] != common[i]:
                    break
                i += 1

            # If in the above while-loop, no character of the word matches with common then return empty string.
            if i == 0:
                return ""

            # Else update the common value to only the first 'i' characters of previous 'common'.
            # The reason is that in the while-loop, only 'i' elements matched.
            # E.g.: ['flower', 'flow', 'flight']. Then initially common will be 'flower'.
            # Then after matching with second word (flow) only the first 4 characters are found ('flow'). So common will become 'flow'.
            # Then after matching the third word (flight) with the updated common (flow), only the first 2 ('fl') characters match.
            # So common becomes 'fl'.
            common = x[:i]

        # Return the longest common prefix.
        return common
