# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        ptr = head
        ptr2 = res

        temp = 0
        while ptr:
            if ptr.val:
                temp += ptr.val
            if temp and not ptr.val:
                ptr2.next = ListNode(temp)
                ptr2 = ptr2.next
                temp = 0
            ptr = ptr.next
        return res.next