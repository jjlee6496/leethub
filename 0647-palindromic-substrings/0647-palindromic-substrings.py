class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, ans = len(s), 0

        def palin_count(left, right):
            count = 0
            while left>=0 and right<n and s[left]==s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(n):
            even = palin_count(i, i+1)
            odd = palin_count(i, i)
            ans += even + odd
        return ans