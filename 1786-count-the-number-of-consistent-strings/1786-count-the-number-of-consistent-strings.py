class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        dic = set(allowed)
        res = len(words)
        for word in words:
            if set(word) - dic:
                res -= 1
        return res
            
