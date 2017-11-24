21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 or l2):
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        head, pre = None, None
        if (l1.val < l2.val):
            head, pre = l1, l1
            l1 = l1.next
        else:
            head, pre = l2, l2
            l2 = l2.next
        while l1 and l2:
            if l1.val > l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        if not l1:
            pre.next = l2
            return head
        if not l2:
            pre.next = l1
            return head