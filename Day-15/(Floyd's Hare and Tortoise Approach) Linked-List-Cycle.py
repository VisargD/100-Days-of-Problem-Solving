"""
Problem Name: Linked List Cycle
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/linked-list-cycle/
"""


"""
APPROACH: (Floyd's Hare and Tortoise Approach)
This approach uses two pointers: hare (fast pointer) and tortoise (slow pointer).
Assume that tortoise and hare are racing on a circular track (in this case, linked list cycle).
Tortoise takes 2 steps at a time and tortoise takes one step at a time. 
So if there is a cycle then at one point after completing one or more rounds, hare will meet the tortoise.
If it happens then it means there is a cycle. 
If the hare reaches Null then it shows that there was no cycle.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # Check if the the linked list is empty. If yes, then return False.
        if not head:
            return False

        # Tortoise will start from head node and hare will start from the next node.
        tortoise = head
        hare = head.next

        # Loop till hare does not meet tortoise.
        while tortoise != hare:

            # Check if current hare is Null or if the next node is Null.
            # If yes, then it means that the hare has reached the end. So there is no cycle.
            # Because if there was a cycle then it would be impossible to reach the end.
            # Return False in such case.
            if not hare or not hare.next:
                return False

            # As tortoise takes 1 step at a time, set tortoise to the next node.
            # As hare takes 2 step at a time, set hare to the next-to-next node.
            tortoise = tortoise.next
            hare = hare.next.next

        # If the hare and tortoise meet, then return True.
        return True
