class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        dic = {}
        for s in (s1 + ' ' + s2).split():
            dic[s] = dic.get(s, 0) + 1

        return list(k for k, v in dic.items() if v == 1)