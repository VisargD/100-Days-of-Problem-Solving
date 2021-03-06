"""
Problem Name: Binary Tree Inorder Traversal
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


"""
APPROACH:
This is a simple Depth First Search approach which includes:
    * Travelling left subtree recursively.
    * Visiting root node.
    * Travelling right subtree recursively.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # inorder will be used to store the inorder traversal.
        inorder = []

        # If the tree is empty then return empty list.
        if not root:
            return []

        # Helper function to perform recursive Depth First Search (DFS).
        def dfs(root, inorder):

            # This is the same as the approach discussed above in the starting.
            # Left->Root->Right.

            # Recursively call the function for the left subtree.
            # If we reached the leftmost node of a subtree then add it to the inorder list.
            # Then visit root and then the right subtree.
            if root.left:
                dfs(root.left, inorder)
            inorder.append(root.val)

            # Recursively call the function for the right subtree.
            if root.right:
                dfs(root.right, inorder)

            # Return the final 'inorder' list.
            return inorder

        # Call the helper function for the input.
        return dfs(root, inorder)
