"""
Problem Name: Robot Return to Origin
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/robot-return-to-origin/
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:

        # This approach is simple 2D-plane approach in which there are x and y coordinates.
        # The robot starts at origin so x and y are 0 initially.
        x = 0
        y = 0

        # For each direction given in moves follow one of the below operations.
        for direction in moves:

            # If the robot moves upwards then the movement is strictly restricted to y-axis.
            # As robot is moving upwards, increment y-axis value. [(0,0) -> (0,1)]
            if direction == 'U':
                y += 1

            # If the robot moves downwards then the movement is strictly restricted to y-axis.
            # As robot is moving downwards, decrement y-axis value. [(0,0) -> (0,-1)]
            elif direction == 'D':
                y -= 1

            # If the robot moves right then the movement is strictly restricted to x-axis.
            # As robot is moving right, increment x-axis value. [(0,0) -> (1,0)]
            elif direction == 'R':
                x += 1

            # If the robot moves left then the movement is strictly restricted to x-axis.
            # As robot is moving left, decrement x-axis value. [(0,0) -> (-1,0)]
            else:
                x -= 1

        # In the end, if x and y are 0 (i.e., origin), then return True.
        if x == 0 and y == 0:
            return True

        # If the last position is not origin then return False.
        else:
            return False
