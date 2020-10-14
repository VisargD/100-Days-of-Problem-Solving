"""
Problem Name: Add Two Numbers
Platform: Leetcode
Difficulty: Medium
Problem Link: https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # l1 and l2 number are intialized to 0 for further calculation.
        # Here count will represent the place of digit (ones, tens, ...)
        l1_number = 0
        l2_number = 0
        count = 1

        # Creating 2 pointers that point to the same object.
        # The idea behind using this is that on every iteration we will add new digit to this linked list and update answer to answer.next .
        # So at the end, answer will point to last node but the temp will be pointing to the first node. So we can return it.
        temp = answer = ListNode(0)

        # Using while-loop to travel from first to last element of linked list.
        while l1:

            # (E.g.: 123 is formed by 3 * 1 + 2 * 10 + 3 * 100).
            # The same logic is used here to form a number from value of linked list nodes.
            # Everytime we increment count (The first will be ones then tens then hundreds and so on ) and change l1 to next node.
            l1_number += (l1.val * count)
            count *= 10
            l1 = l1.next

        # Again setting count to 1.
        # Repeating the above process for l2 linked list.
        count = 1
        while l2:
            l2_number += (l2.val * count)
            count *= 10
            l2 = l2.next

        # Add both the digits formed from the linked list.
        total = l1_number + l2_number

        # If total = 0 then simply return a single node linked list.
        if total == 0:
            return ListNode(0)

        # E.g.: Mathematical way to get last digit is to perform modulo 10. (123 % 10 = 3)
        # E.g. Mathematical way to remove last digit is floor division by 10. (123 // 10 = 12)
        # If total is greater than 0 then by performing above steps, add digits to linked list one by one in reverse order.
        while total != 0:
            answer.next = ListNode(total % 10)
            answer = answer.next
            total //= 10

        # temp still point to the first node of answer linked list.
        # E.g. : If the final number is 123 then temp = 0->3->2->1. Here first element is 0 because we initialized the linked list with a node of value 0 at starting.
        # So returning temp.next will point to the required node after the zero node.
        return temp.next


"""
EXAMPLE: 

l1_number = 123
l2_number = 123
total = 246

In this case "answer" will currently point at last node, i.e, 2.
But in the beginning, we intialized both "answer" and "temp" to point to same object.

So, temp = 0->6->4->2.
That is why I returned temp.next
"""
