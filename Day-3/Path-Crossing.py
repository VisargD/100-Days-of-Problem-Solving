"""
Problem Name: Path Crossing
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/path-crossing/
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:

        # Create a dictionary with origin (0, 0) as a key and its occurence (initially 1) as its value.
        # x and y represents coordinates.
        points = {(0, 0): 1}
        x = 0
        y = 0

        # Using for-loop to traverse through the string.
        for direction in path:

            # If direction is North, then we move upwards. So increment y-axis value.
            if direction == 'N':
                y += 1

            # If direction is East, then we move right. So increment x-axis value.
            elif direction == 'E':
                x += 1

            # If direction is South, then we move downwards. So decrement y-axis value.
            elif direction == 'S':
                y -= 1

            # If direction is West, then we move left. So decrement x-axis value.
            elif direction == 'W':
                x -= 1

            # In every for-loop iteration, check if the current (x, y) pair is in dictionary.
            # If it is present then return True. Else add the new entry for (x, y) in dictionary.
            if (x, y) in points:
                return True
            else:
                points[(x, y)] = 1

        # If during the whole for-loop, none of the pair occurs for 2 times then return False in the end.
        return False
