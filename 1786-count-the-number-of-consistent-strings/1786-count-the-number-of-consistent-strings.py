class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        dic = set(allowed)
        res = 0
        for word in words:
            if set(word) - dic:
                continue
            res += 1
        return res
            
