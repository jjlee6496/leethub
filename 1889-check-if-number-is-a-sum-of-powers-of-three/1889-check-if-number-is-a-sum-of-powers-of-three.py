class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        def dfs(i, curr):
            if curr == 0:
                return True
            
            if curr < 0 or i > 15:
                return False
            
            if dfs(i + 1, curr - 3 ** i):
                return True
            
            return dfs(i + 1, curr)
        return dfs(0, n)
            

            