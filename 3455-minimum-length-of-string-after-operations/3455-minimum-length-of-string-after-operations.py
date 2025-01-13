class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        cnt = Counter(s)
        
        for v in cnt.values():
            if v % 2:
                ans += 1
            else:
                ans += 2
        return ans