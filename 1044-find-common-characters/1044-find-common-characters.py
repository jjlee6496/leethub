class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for c in set(words[0]):
            cnt = min([x.count(c) for x in words])
            res.extend([c]*cnt)
        return res