"""
Problem name: Two Sum
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # This is a simple but not so optimal approach where I used two for loops to check if the sum matches the target.
        for i in range(len(nums)):
            remaining = target - nums[i]
            for j in range(len(nums)):
                if nums[j] == remaining and i != j:
                    return [i, j]
