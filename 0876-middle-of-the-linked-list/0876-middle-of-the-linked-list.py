# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        n = 0
        while fast.next:
            fast = fast.next
            n += 1
        
        for _ in range(n//2):
            slow = slow.next
        return slow.next if n%2 else slow