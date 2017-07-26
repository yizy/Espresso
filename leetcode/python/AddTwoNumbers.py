# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        dummy = l = ListNode(0)
        while l1 or l2 or c:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            s = x + y + c
            c = s / 10
            l.next = ListNode(s % 10)
            
            l = l.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
