
# You are given two non-empty linked lists 
# representing two non-negative integers. The digits are stored 
# in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        carry = 0

        # we include the or carry since in our last it could have another node

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # compute new digit
            val = v1 + v2 + carry
            # if like 17
            carry = val // 10 #provide us with 10's place to carry
            val = val % 10 # will provide us the 1's place

            cur.next = ListNode(val)
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next