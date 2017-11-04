#2. Add Two Numbers
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

# 思路：先求l1和l2公共部分的和，再对较长的一个链表做单独运算处理

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
        head, p1, p2 = ListNode(0), l1, l2
        tail = head
        # 进位
        carry = 0 
#       p1、p2均不为空  
        while p1 and p2:
            sum = p1.val + p2.val + carry 
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            tail.next = ListNode(sum)
            tail = tail.next
            p1 = p1.next
            p2 = p2.next
        if p2: 
            p1 = p2
        while p1:
            sum = p1.val + carry
            if sum > 9:
                sum -= 10
                carry = 1
            else:
                carry = 0
            tail.next = ListNode(sum)
            tail = tail.next
            p1 = p1.next
        if carry == 1:
            tail.next = ListNode(1)
            tail = tail.next
        tail.next = None
        return head.next