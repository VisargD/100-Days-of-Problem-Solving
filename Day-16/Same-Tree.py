"""
Problem Name: Same Tree
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/same-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # Helper function to perform Recursive Depth First Search.
        def dfs(p, q):

            # If both the nodes are None then return True.
            if not p and not q:
                return True

            # If only one of the nodes is None or if value of both the nodes do not match, then they are not the same tree.
            # Return False.
            if not p or not q or p.val != q.val:
                return False

            # Else perform recursive search on the left and right subtree of both the trees.
            # Here every node of both the trees are matched. And if at any point, one of them does not match then it will return False.
            # Here 'AND' is used because if any one of the subtree has a mismatched node then it will return False
            # 'AND' will preserve that False (FALSE and TRUE = FALSE).
            else:
                answer = dfs(p.left, q.left) and dfs(p.right, q.right)
                return answer

        # Call the function for p and q.
        return dfs(p, q)
