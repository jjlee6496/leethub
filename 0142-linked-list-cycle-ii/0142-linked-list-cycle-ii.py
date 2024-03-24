# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        turtle = hare = head
        iscycle = False
        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
            if turtle == hare:
                iscycle = True
                break
        if not iscycle:
            return None
        
        ptr1 = head
        ptr2 = turtle

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
        
