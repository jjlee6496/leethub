class Solution:
    def minimumLength(self, s: str) -> int:
        q = deque(list(s))
        while q:
            if q[0] == q[-1] and len(q)>1:
                pre, suf = q.popleft(), q.pop()
                while q and q[0] == pre:
                    q.popleft()
                while q and q[-1] == suf:
                    q.pop()
            else:
                break
        return len(q)
            