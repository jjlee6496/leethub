# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(m, n):
            if n == 0:
                return m
            return gcd(n, m%n)

        curr = head
        while curr.next:
            temp = ListNode(gcd(curr.val, curr.next.val))
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        return head