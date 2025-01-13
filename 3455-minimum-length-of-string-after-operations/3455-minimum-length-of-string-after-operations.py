class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cnt = Counter(s)
        for l in cnt:
            while cnt[l] > 2:
                cnt[l] -= 2
                n -= 2
        return n