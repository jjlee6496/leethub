# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        chunk_size, remain = length // k, length % k
        result = []
        curr = head
        for i in range(k):
            result.append(curr)
            size = chunk_size + (1 if i < remain else 0 )
            for _ in range(size - 1):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
        return result