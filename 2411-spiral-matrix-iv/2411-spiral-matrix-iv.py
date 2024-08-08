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
        res = [[-1]*n for _ in range(m)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_ind = 0
        x, y = 0, 0
        while head.next:
            res[x][y] = head.val
            dx, dy = direction[d_ind]
            nx, ny = x + dx, y + dy
            while nx < 0 or nx >= m or ny < 0 or ny >= n or res[nx][ny] != -1:
                d_ind = (d_ind + 1) % 4
                dx, dy = direction[d_ind]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
            head = head.next
        res[x][y] = head.val
        return res


