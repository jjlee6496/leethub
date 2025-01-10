class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        res = 0
        for word in words:
            if word[:len(pref)] == pref:
                res += 1
        return res