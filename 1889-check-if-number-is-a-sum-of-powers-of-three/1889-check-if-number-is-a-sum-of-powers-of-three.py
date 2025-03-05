class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def dfs(i, cur):
            if cur == n:
                return True
            if cur > n or i > 14:
                return False
            
            if dfs(i + 1, cur + 3 ** i):
                return True
            
            # skip
            return dfs(i + 1, cur)
        
        return dfs(0, 0)