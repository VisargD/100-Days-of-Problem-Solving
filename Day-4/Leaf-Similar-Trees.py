"""
Problem Name: Leaf-Similar Trees
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/leaf-similar-trees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        # Creating 2 empty list to keep track of leaf nodes of both the trees.
        root1_leaves = []
        root2_leaves = []

        # Helper function that performs recursive DFS to find the leaf node.
        def find_leaf(root: TreeNode, root_list: list) -> list:

            # If both left and right are None then it means that the node is a leaf node.
            # So append its value in the list.
            if not root.left and not root.right:
                root_list.append(root.val)

            # If both sides are not None then check if left is None or not.
            # If it is not None then call the helper function for the left node.
            # This takes care of situation when it is necessary to check whether left is present or not. [1, null, 2].
            if root.left:
                find_leaf(root.left, root_list)

            # If both sides are not None then check if right is None or not.
            # If it is not None then call the helper function for the right node.
            # This takes care of situation when it is necessary to check whether right is present or not. [1, 2, null].
            if root.right:
                find_leaf(root.right, root_list)

            # Finally return the list with leaf node values.
            return root_list
        
        # Pythonic way to check if two lists are equal or not.
        # Call the helper function for both the tree nodes and find the leaves list and compare it.
        return find_leaf(root1, root1_leaves) == find_leaf(root2, root2_leaves)
