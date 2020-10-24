"""
Problem Name: Linked List Cycle
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # Creating an empty dictionary to store all the node references.
        # It will be used to check if any node has already been visited.
        hash_table = {}

        # Traversing the list till last node.
        while head:

            # Here node is stored in the dictionary and not its value. So it will be unique.

            # If the current node is already in the dictionary then it proves that there is a linked list cycle.
            # So return True.
            if head in hash_table:
                return True

            # If the node is not present in the dictionary then make a new entry to mark it as visited.
            else:
                hash_table[head] = 1

            # Change the head to the next node.
            head = head.next

        # If no cycle is found above then return False.
        return False
