# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        res = ListNode()
        ptr = res
        while head:
            while head and head.val in nums:
                head = head.next
            ptr.next = head
            ptr = ptr.next
            if not head:
                break
            head = head.next
        return res.next