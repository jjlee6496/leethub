class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i*i for i in range(1, int(math.sqrt(n))+1)]
        def bfs(n):
            q = deque([(n, 0)])
            while q:
                curr, cnt = q.popleft()
                for square in squares:
                    diff = curr - square
                    if diff == 0:
                        return cnt + 1
                    elif diff < 0:
                        break
                    q.append((diff, cnt+1))

            return -1
        return bfs(n)