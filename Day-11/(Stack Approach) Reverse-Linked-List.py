"""
Problem Name: Reverse Linked List
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Using a list to store all the value of the linked list.
        stack = []

        # Using while loop to iterate through a linked list until head.next is not Null (i.e., until last node).
        while head:

            # Add node values to the list and move head to the next node.
            # This will store all the values one by one in the list.
            stack.append(head.val)
            head = head.next

        # Creating two pointers that point to the same ListNode object.
        dummy = answer = ListNode(0)

        # Now to add the values in reverse order we will pop the last element from stack and add it to the newly created 'answer'.
        # And then move 'answer' to the newly created node so that further nodes can be added in the same way.
        while len(stack) != 0:
            answer.next = ListNode(stack.pop())
            answer = answer.next

        # As both answer and dummy pointed to the same object, we can access linked list using both of them.
        # After adding all the values in reverse order, 'answer' will point at the last node.
        # But we need to return the starting.
        # In this case, 'dummy' is used as it is still pointing at the beginning.
        # dummy = 0 -> reverse_order_val -> reverse_order_val -> reverse_order_val...
        # So by returning dummy.next, the first '0' is skipped and we get the required answer.
        return dummy.next


# Here, answer is initialized with a node with value 0.
# For example, after adding 5,4,3,2,1 in reverse order (0-5-4-3-2-1), 'answer' will point at '1' node (last node).
# But 'dummy' still points at initial node (Inital node is ListNode(0) as we declared in the code above).
# So, dummy still point at starting of 0->5->4->3->2->1. So dummy.next gives the required list.
