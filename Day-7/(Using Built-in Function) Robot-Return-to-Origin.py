"""
Problem Name: Robot Return to Origin
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/robot-return-to-origin/
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:

        # In order to return back to origin, the number of left and right move should be equal. And number of up and down move should be equal.
        # This if-statement checks for the above condition and return True if satisfied. Else False.
        if moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L'):
            return True
        else:
            return False
