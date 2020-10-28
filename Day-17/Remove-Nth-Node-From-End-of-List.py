"""
Problem Name: Remove Nth Node From End of List
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Check if the linked list has only one element.
        # If yes then after removing it, the linked list will be empty. So return None.
        if not head.next:
            return None

        # Initializing length to 0.
        # Creating a linked list node with value 0 and then assigning its next pointer to head node.
        # So now dummy = temp = 0 -> head.
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy

        # While-loop to count the length (number of nodes).
        while head:
            length += 1
            head = head.next

        # Setting the target to length - n. This will help us in determining the preceeding node of the node that needs to be removed.
        # Setting counter to 0.
        target = length - n
        count = 0

        # Until count is not equal to target, keep moving dummy to the next node and increment count.
        # This will loop until it reaches the node before the node that needs to be removed.
        while count != target:
            dummy = dummy.next
            count += 1

        # When the count and target becomes equal then we have reached the node before the node that needs to be deleted.
        # So set the next pointer to the next-to-next node. This is the deletion step.
        # Here dummy start from 0 node. So even if the first element needs to be removed, it can be done successfully.
        dummy.next = dummy.next.next

        # Return temp.next
        return temp.next


# Here, dummy plays a very important role to cover corner case of when list contains only 1 element and 1 element needs to be deleted.
