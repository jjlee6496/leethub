# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        temp = prev = post = list1

        for _ in range(b + 1):
            post = post.next

        for _ in range(a-1):
            prev = prev.next
        prev.next = list2
        
        while temp.next:
            temp = temp.next
        temp.next = post
        
        return list1
        
        