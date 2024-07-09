# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def critical(self, prev, curr, nxt):
        return prev.val < curr.val > nxt.val or prev.val > curr.val < nxt.val

    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prev, curr = head, head.next
        nxt = curr.next

        first_crit = 0
        prev_crit = 0

        max_dist = -1
        min_dist = float('inf')
        i = 1 # curr index
        while nxt:
            if self.critical(prev, curr, nxt):
                if first_crit:
                    max_dist = i - first_crit
                    min_dist = min(min_dist, i - prev_crit)
                else:
                    first_crit = i
                prev_crit = i
            i += 1
            prev, curr, nxt = curr, nxt, nxt.next
        
        if min_dist == float('inf'):
            min_dist = -1
        
        return [min_dist, max_dist]