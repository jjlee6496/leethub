class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key = lambda x: len(x))
        res = set()
        for i in range(len(words)):
            temp = words[i]
            for j in range(i + 1, len(words)):
                if temp in words[j]:
                    res.add(temp)
        return list(res)