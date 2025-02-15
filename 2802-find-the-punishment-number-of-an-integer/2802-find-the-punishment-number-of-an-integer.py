class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_punish(i, curr, target, string):
            if i >= len(string) and curr == target:
                return True
            
            for j in range(i, len(string)):
                if is_punish(j + 1, curr + int(string[i:j+1]), target, string):
                    return True

            return False
        

        res = 0
        for i in range(1, n + 1):
            if is_punish(0, 0, i, str(i * i)):
                res += (i * i)
        
        return res