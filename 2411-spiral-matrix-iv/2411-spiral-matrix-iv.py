# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ind = 0
        res = [[-1]*n for _ in range(m)]
        x, y = 0, -1
        while head:
            dx, dy = directions[ind]
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and res[nx][ny] < 0:
                res[nx][ny] = head.val
                head = head.next
                x, y = nx, ny
            else:
                ind = (ind + 1) % 4
        return res