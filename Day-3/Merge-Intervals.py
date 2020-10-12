"""
Problem Name: Merge Intervals
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/merge-intervals/
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Using answer list to store final merged intervals. And setting index to 0.
        answer = []
        index = 0

        # Checking the edge case where the list is empty. If yes, then return [].
        if len(intervals) == 0:
            return []

        # Sorting the intervals list with the start element of each interval as key in ascending order.
        intervals = sorted(intervals, key=lambda x: x[0])

        # Setting initial start and end value as the starting and ending value of first interval.
        start = intervals[0][0]
        end = intervals[0][1]

        # Using while-loop until index is not equal to len(intervals).
        while index != len(intervals):

            #  Check If the index is not the last index as it would give out of bounds error while checking index + 1.
            if index != len(intervals) - 1:

                # If the current end value is greater than the start value of next interval then,
                # Merge the interval and set end as the maximum of (current max and end of the next interval).
                # Also set the start to minimum of (current start and start of next interval).
                # Increment index.
                if end >= intervals[index + 1][0]:
                    end = max(intervals[index + 1][1], end)
                    start = min(intervals[index + 1][0], start)
                    index += 1

                # If current end is not greater or equal to next interval's start then it means they can't be merged.
                # Simple append the current [start, end] to answer and set start and end values equal to next interval.
                # Increment index.
                else:
                    answer.append([start, end])
                    start = intervals[index + 1][0]
                    end = intervals[index + 1][1]
                    index += 1

            # If index is the last index then we can't check the next interval as it is out of bound.
            # So simply add the current start and end value to answer list and increment index to break the while loop.
            else:
                answer.append([start, end])
                index += 1

        # Return the Final Answer.
        return answer
