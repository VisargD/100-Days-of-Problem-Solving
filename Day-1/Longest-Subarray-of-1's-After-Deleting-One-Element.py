"""
Problem name: Longest Subarray of 1's After Deleting One Element
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # zero tracks the latest index of 0 in the array.
        zero = -1

        # k tracks the deletion counter
        k = 1

        # maxi tracks the maximum count value. And count tracks the current count value of 1's.
        maxi = 0
        count = 0
        i = 0

        # Using while loop to iterate through the index value.
        while i != len(nums):
             
            if nums[i] == 0:
                # If value at index is 0 then check the deletion counter (k).
                # If k is 0 then change the index (i) to latest zero index + 1.
                # Change the latest zero index to current index value.
                # Check and set the maximum value. And set k to 1 again for further iterations.
                if k == 0:
                    i = zero + 1
                    zero = i
                    maxi = max(count, maxi)
                    count = 0
                    k = 1

                # If k is not 0 then simply decrement k and increment index.
                # Also change the latest zero index to current value of index.
                else:
                    k -= 1
                    zero = i
                    i += 1   

            # If value at index is not 0 then simply increment the count and index.                 
            else:
                count += 1
                i += 1

        # Finding the max value out of the 2 values.
        # If the last element of array is not 0 then the maxi value would not have considered the latest count value.
        # So this condition helps in taking care of this situation.
        maxi = max(count, maxi)

        # If every element is 1 then maxi will be equal to length of array.
        # But we need to delete one element (compulsory) so return maxi - 1.
        if maxi == len(nums):
            return maxi - 1

        # Else return the maxi value.
        else:
            return maxi