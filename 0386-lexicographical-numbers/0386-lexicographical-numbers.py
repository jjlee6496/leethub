class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        i = 1
        while len(res) < n:
            res.append(i)
            if 10 * i <= n:
                i *= 10
            else:
                while i == n or i % 10 == 9:
                    i //= 10
                i += 1
        return res