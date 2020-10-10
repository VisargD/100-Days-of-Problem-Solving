"""
Problem name: Two Sum
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Creating a dictionary to store number along with its index if the (target - value) is not found in this dict.
        my_dict = {}
        
        # Using for loop.
        for i in range(len(nums)):

            # on every iteration, simply checking if (target - value) is present in the dict or not.
            # If present then simply return the current index and the value for the remaining value entry in dict
            if target - nums[i] in my_dict:
                return [my_dict[target-nums[i]], i]

            # If the remaining value (i.e, target - nums[i]) is not present then,
            # Simply add the current value (nums[i]) as a key and the index as the value in the dict.
            else:
                my_dict[nums[i]] = i

    # As the problem states, there will always be one exact solution. So the output will surely be generated in the above loop.    