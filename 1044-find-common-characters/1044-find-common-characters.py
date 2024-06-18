class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        dic = Counter(words[0])
        for word in words[1:]:
            dic = Counter(word) & dic
        for k, v in dic.items():
            for _ in range(v):
                res.append(k)
        return res